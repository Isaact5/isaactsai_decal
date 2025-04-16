import pandas as pd
import sys

# Load the hydrogen spectrum data
filename = 'hydrogen_spectrum.csv'
# Assign column names manually (replace with the correct order)
column_names = [
    'Index', 'Blank1', 'Observed Wavelength (nm)', 'Uncertainty (nm)', 'Blank2',
    'Wavenumber (cm-1)', 'Intensity', 'Lower Level (n)', 'Blank3', 'Energy Levels',
    'Lower Level', 'Lower Term', 'Lower J', 'Upper Level (n)', 'Blank4', 'Blank5',
    'Blank6', 'Transition ID', 'Blank7'
]
df = pd.read_csv(filename, skiprows=3, names=column_names)

# Print the actual column names to help with filtering
print('Actual column names:')
for col in df.columns:
    print(f'- {col}')

# Use the exact column names from your output
relevant_cols = [
    'Observed Wavelength (nm)',
    'Lower Level (n)',
    'Upper Level (n)',
    'Uncertainty (nm)'
]
df = df[relevant_cols]

# Minimal filtering: only drop rows with missing or non-numeric values in critical columns
for col in ['Observed Wavelength (nm)', 'Lower Level (n)', 'Upper Level (n)']:
    df = df[pd.to_numeric(df[col], errors='coerce').notnull()]
df = df.dropna(subset=['Observed Wavelength (nm)', 'Lower Level (n)', 'Upper Level (n)'])

# Convert quantum numbers to integers
for col in ['Lower Level (n)', 'Upper Level (n)']:
    df[col] = df[col].astype(int)

# Keep only rows where n2 > n1 (valid Rydberg transitions)
initial_len = len(df)
df = df[df['Upper Level (n)'] > df['Lower Level (n)']]
filtered_len = len(df)
if filtered_len < initial_len:
    print(f"Filtered out {initial_len - filtered_len} rows where n2 <= n1.")

# Remove duplicate rows
before_dupes = len(df)
df = df.drop_duplicates()
after_dupes = len(df)

# Print cleaned data preview and summary
print('Cleaned data preview:')
print(df.head())
print(f'Number of rows after cleaning: {len(df)}')
print(f'Removed {before_dupes - after_dupes} duplicate rows.')

# Export cleaned data to CSV
output_filename = 'hydrogen_spectrum_cleaned.csv'
df.to_csv(output_filename, index=False)
print(f'Exported cleaned data to {output_filename} ({len(df)} rows).')

# TODO: Continue with Rydberg analysis and fitting. 