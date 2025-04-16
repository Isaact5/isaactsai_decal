import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import os

# Load the cleaned hydrogen spectrum data
# Use absolute path so the script works from any directory
script_dir = os.path.dirname(os.path.abspath(__file__))
datafile = os.path.join(script_dir, 'hydrogen_spectrum_cleaned.csv')
df = pd.read_csv(datafile)

# Rydberg formula for hydrogen (in nm):
def rydberg_wavelength(n1, n2, R):
    # Returns wavelength in nm given n1, n2, and Rydberg constant R (in cm^-1)
    # 1/λ = R (1/n1^2 - 1/n2^2) => λ = 1 / (R * (1/n1^2 - 1/n2^2))
    inv_lambda = R * (1.0 / n1**2 - 1.0 / n2**2)
    # Convert from cm^-1 to nm: λ (nm) = 1e7 / inv_lambda (cm^-1)
    return 1e7 / inv_lambda

# Prepare data for fitting
n1 = df['Lower Level (n)'].values
n2 = df['Upper Level (n)'].values
wavelength_obs = df['Observed Wavelength (nm)'].values
uncertainty = df['Uncertainty (nm)'].values if 'Uncertainty (nm)' in df.columns else np.ones_like(wavelength_obs)

# Diagnostic: Plot observed vs. calculated wavelengths using accepted Rydberg constant
accepted_R_H = 109677.0
wavelength_calc = rydberg_wavelength(n1, n2, accepted_R_H)
plt.figure(figsize=(8, 5))
plt.scatter(wavelength_obs, wavelength_calc, alpha=0.6, label='Data')
plt.plot([wavelength_obs.min(), wavelength_obs.max()], [wavelength_obs.min(), wavelength_obs.max()], 'r--', label='y = x (perfect)')
plt.xlabel('Observed Wavelength (nm)')
plt.ylabel('Calculated Wavelength (nm) (accepted $R_H$)')
plt.title('Observed vs. Calculated Wavelengths (Accepted $R_H$)')
plt.legend()
plt.tight_layout()
plt.show()

# Diagnostic: Print sample n1, n2, and calculated wavelengths
print("Sample n1, n2, observed_wavelength, calculated_wavelength (accepted R_H):")
for i in range(min(10, len(n1))):
    print(f"n1={n1[i]}, n2={n2[i]}, obs={wavelength_obs[i]:.3f} nm, calc={wavelength_calc[i]:.3f} nm")

# Define a wrapper for curve_fit (n1, n2 as arrays, R as parameter)
def rydberg_fit_func(X, R):
    n1, n2 = X
    return rydberg_wavelength(n1, n2, R)

# Placeholder for curve fitting and results interpretation
# TODO: Fit the Rydberg constant using curve_fit, plot results, and interpret

if __name__ == '__main__':
    print('Loaded cleaned data:')
    print(df.head())

    # Initial guess for Rydberg constant (in cm^-1)
    R_H_initial = 109677.0
    
    # Fit the Rydberg formula to the observed data
    try:
        popt, pcov = curve_fit(
            rydberg_fit_func,
            (n1, n2),
            wavelength_obs,
            sigma=uncertainty,
            absolute_sigma=True,
            p0=[R_H_initial],
            maxfev=10000
        )
        R_H_fit = popt[0]
        R_H_err = np.sqrt(np.diag(pcov))[0]
        print(f"\nBest-fit Rydberg constant: R_H = {R_H_fit:.2f} ± {R_H_err:.2f} cm⁻¹")
        print(f"Accepted value: R_H = {accepted_R_H} cm⁻¹")
        print(f"Difference: {R_H_fit - accepted_R_H:.2f} cm⁻¹")
    except Exception as e:
        print(f"Curve fitting failed: {e}")
        exit(1)

    # Calculate fitted wavelengths
    wavelength_fit = rydberg_fit_func((n1, n2), R_H_fit)

    # Plot observed vs. fitted wavelengths
    plt.figure(figsize=(8, 5))
    plt.scatter(wavelength_obs, wavelength_fit, alpha=0.6, label='Data')
    plt.plot([wavelength_obs.min(), wavelength_obs.max()], [wavelength_obs.min(), wavelength_obs.max()], 'r--', label='y = x (perfect fit)')
    plt.xlabel('Observed Wavelength (nm)')
    plt.ylabel('Fitted Wavelength (nm)')
    plt.title('Observed vs. Fitted Wavelengths (Hydrogen Spectrum)')
    plt.legend()
    plt.tight_layout()
    plt.show()

    # --- Additional Analysis ---
    # 1. Plot residuals
    residuals = wavelength_obs - wavelength_fit
    plt.figure(figsize=(8, 4))
    plt.scatter(wavelength_obs, residuals, alpha=0.6)
    plt.axhline(0, color='r', linestyle='--')
    plt.xlabel('Observed Wavelength (nm)')
    plt.ylabel('Residual (Observed - Fitted) [nm]')
    plt.title('Residuals of Fit')
    plt.tight_layout()
    plt.show()

    # 2. Calculate reduced chi-squared
    chi2 = np.sum((residuals / uncertainty) ** 2)
    dof = len(wavelength_obs) - 1  # number of data points minus number of fit parameters
    red_chi2 = chi2 / dof
    print(f"Reduced chi-squared: {red_chi2:.2f}")

    # 3. Identify outliers (e.g., |residual| > 3 * uncertainty)
    outlier_mask = np.abs(residuals) > 3 * uncertainty
    n_outliers = np.sum(outlier_mask)
    if n_outliers > 0:
        print(f"\nIdentified {n_outliers} outliers (|residual| > 3σ):")
        print(df[outlier_mask][['Observed Wavelength (nm)', 'Lower Level (n)', 'Upper Level (n)', 'Uncertainty (nm)']])
    else:
        print("\nNo outliers with |residual| > 3σ.")

uncertainty_threshold = 0.1  # nm 