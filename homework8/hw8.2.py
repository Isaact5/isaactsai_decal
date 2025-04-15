import pandas

def analyze_stars(filename='stars.csv'):

    df = pandas.read_csv(filename)
    
    #pring stars first 5 rows
    print("First 5 rows:")
    print(df.head())
    print("\nDataset dimensions (rows, columns):")
    print(df.shape)
    print("\nColumn names and data types:")
    print(df.dtypes)
    
    #average mass and temperature
    print(f"Average mass: {df['Mass (M☉)'].mean():.2f}")
    print(f"Average temperature: {df['Temperature (K)'].mean():.2f}")
    
    #star with largest radius
    print("\nStar with largest radius:")
    largest_radius = df.loc[df['Radius (R☉)'].idxmax()]
    print(largest_radius)
    
    #number of M-type stars
    m_type_count = df[df['Spectral_Type'].str.startswith('M', na=False)].shape[0]
    print(f"\nNumber of M-type stars: {m_type_count}")
    
    #3 closest stars and sort
    print("\n3 closest stars:")
    closest_stars = df.nsmallest(3, 'Distance (ly)')
    print(closest_stars)
    
    #save M-type stars to new file
    m_type_stars = df[df['Spectral_Type'].str.startswith('M', na=False)]
    m_type_stars.to_csv('m_type_stars.csv', index=False)
    print("\nM-type stars have been saved to m_type_stars.csv")

if __name__ == "__main__":
    analyze_stars()