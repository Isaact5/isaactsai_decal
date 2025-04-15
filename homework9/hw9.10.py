import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from astropy.table import Table
from scipy import optimize
import os

# read
downloads_path = os.path.expanduser("~/Downloads")
data_path = os.path.join(downloads_path, "global_CCl4_MM.dat")
data = Table.read(data_path, format='ascii')

# convert to dataframe
df = pd.DataFrame({
    'date': data[data.colnames[0]],  # First column
    'concentration': data[data.colnames[1]],  # Second column
    'concentration_sd': data[data.colnames[2]]  # Third column
})

# plot
plt.figure(figsize=(12, 6))
plt.errorbar(df['date'], df['concentration'], yerr=df['concentration_sd'],
            fmt='.', label='Data', alpha=0.5)

# fit linear model
def linear_model(x, m, b):
    return m * x + b

# initial guesses
p0 = [0, np.mean(df['concentration'])]

# fit the model
popt, pcov = optimize.curve_fit(linear_model, df['date'], df['concentration'], 
                              p0=p0, sigma=df['concentration_sd'])

# generate points for fitted line
x_fit = np.linspace(df['date'].min(), df['date'].max(), 100)
y_fit = linear_model(x_fit, *popt)

# plot fitted line
plt.plot(x_fit, y_fit, 'r-', label='Fit')
plt.xlabel('Date')
plt.ylabel('Global Mean Concentration')
plt.title('CCl4 Global Mean Concentration Over Time')
plt.legend()
plt.grid(True)
plt.show()

# calculatereduced chi-squared
residuals = df['concentration'] - linear_model(df['date'], *popt)

# plot residuals
plt.figure(figsize=(12, 4))
plt.errorbar(df['date'], residuals, yerr=df['concentration_sd'], fmt='.', alpha=0.5)
plt.axhline(y=0, color='r', linestyle='-', label='y=0')
plt.xlabel('Date')
plt.ylabel('Residuals')
plt.title('Residuals Plot')
plt.grid(True)
plt.legend()
plt.show()

# calculate reduced chi-squared
chi_squared = np.sum((residuals / df['concentration_sd'])**2)
dof = len(df) - 2  # degrees of freedom
reduced_chi_squared = chi_squared / dof

# print results
print("\nFit Params:")
param_names = ['Slope', 'Intercept']
errors = np.sqrt(np.diag(pcov))
for name, value, error in zip(param_names, popt, errors):
    print(f"{name}: {value:.2f} ± {error:.2f}")

print(f"\nFit Equation: y = ({popt[0]:.2f} ± {errors[0]:.2f})x + ({popt[1]:.2f} ± {errors[1]:.2f})")
print(f"Reduced Chi squared: {reduced_chi_squared:.3f}")

