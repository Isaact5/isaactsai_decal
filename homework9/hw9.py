import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize

# read
downloads_path = os.path.expanduser("~/Downloads")
csv_path = os.path.join(downloads_path, "GlobalLandTemperaturesByState.csv")
df = pd.read_csv(csv_path)

#filter
df = df[['dt', 'AverageTemperature', 'State']]

df['dt'] = pd.to_datetime(df['dt'])
df = df[df['dt'].dt.year > 2000]

states_of_interest = ['Wyoming', 'Nebraska', 'South Dakota']
df = df[df['State'].isin(states_of_interest)]

#check
#print(f"Shape of filtered dataframe: {df.shape}")

#1.2
avg_temp_by_date = df.groupby('dt')['AverageTemperature'].mean().reset_index()
print("\nShape after grouping by date:", avg_temp_by_date.shape)

# 1.3
plt.figure(figsize=(12, 6))
plt.plot(avg_temp_by_date['dt'], avg_temp_by_date['AverageTemperature'])
plt.xlabel('Date')
plt.ylabel('Average Temperature (°C)')
plt.title('Average Temperature for Wyoming, Nebraska, and South Dakota')
plt.grid(True)
plt.show()

# 1.4: Convert dates to numerical values (years since 2000)
avg_temp_by_date['date_numeric'] = (avg_temp_by_date['dt'] - pd.Timestamp('2000-01-01')).dt.total_seconds() / (365.25 * 24 * 3600)

#check
#print(avg_temp_by_date.head())

#1.5 - didn't use suggested form - at this point it's almost natural due to 5BL... sigh
def temperature_model(x, amplitude, period, phase, offset):
    # A * cos(2π * x/P + φ) + C
    return amplitude * np.cos(2 * np.pi * x / period + phase) + offset

# Initial parameter guesses:
# amplitude: half temperature range
# period: 1 year
# phase: -π/2 (so cosine peaks in summer)
# offset: mean temp
initial_guess = [
    (avg_temp_by_date['AverageTemperature'].max() - avg_temp_by_date['AverageTemperature'].min()) / 2,  # amplitude
    1.0, 
    -np.pi/2,
    avg_temp_by_date['AverageTemperature'].mean()
]

# 1.6
x_data = avg_temp_by_date['date_numeric']
y_data = avg_temp_by_date['AverageTemperature']
popt, pcov = optimize.curve_fit(temperature_model, x_data, y_data, p0=initial_guess)

#generates 
x_fit = np.linspace(x_data.min(), x_data.max(), 1000)
y_fit = temperature_model(x_fit, *popt)

# 1.7
#plot fit
plt.figure(figsize=(12, 6))
plt.scatter(avg_temp_by_date['dt'], y_data, label='Data', alpha=0.5, color='blue')
plt.plot(pd.Timestamp('2000-01-01') + pd.to_timedelta(x_fit * 365.25 * 24 * 3600, unit='s'),y_fit, 'r-', label='Fitted Curve', linewidth=2)
plt.xlabel('Date')
plt.ylabel('Average Temperature (°C)')
plt.title('Temperature Data and Fitted Curve')
plt.grid(True)
plt.legend()
plt.show()

# 1.8
param_names = ['Amplitude', 'Period', 'Phase', 'Offset']
errors = np.sqrt(np.diag(pcov))

#1.9
print("\nFitted Parameters and Errors:")
for name, value, error in zip(param_names, popt, errors):
    print(f"{name}: {value:.3f} ± {error:.3f}")

print("\nFinal Equation:")
print(f"T(t) = {popt[0]:.3f} * cos(2π * t/{popt[1]:.3f} + {popt[2]:.3f}) + {popt[3]:.3f}")