import pandas as pd

def get_input_data():
    # Prompt user for the number of concerts
    num_concerts = int(input("Enter the number of concerts: "))
    
    # Initialize empty lists for the columns
    artists = []
    venues = []
    dates = []
    
    # Collect data for each concert
    for i in range(num_concerts):
        artist = input(f"Enter artist for concert {i + 1}: ")
        venue = input(f"Enter venue for concert {i + 1}: ")
        date_input = input(f"Enter date for concert {i + 1} (format: YYYY-MM-DD): ")
        
        try:
            # Convert date to datetime format
            date = pd.to_datetime(date_input)
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            continue
        
        artists.append(artist)
        venues.append(venue)
        dates.append(date)
    
    # Return the collected data as a DataFrame
    return pd.DataFrame({
        'artist': artists,
        'venue': venues,
        'date': dates
    })

def create_concert_table(df):
    # Extract year and month from the 'date' column
    df['year_month'] = df['date'].dt.to_period('M')
    
    # Count concerts per (artist, venue), per year-month
    concert_counts = df.groupby(['year_month', 'artist', 'venue']).size().reset_index(name='concert_count')
    
    # Create the cross product of artists and venues
    artists = df['artist'].unique()
    venues = df['venue'].unique()
    cross_product = pd.MultiIndex.from_product([artists, venues], names=['artist', 'venue'])
    
    # Create the wide table with year-month as rows and (artist, venue) as columns
    pivot_table = concert_counts.pivot_table(index='year_month', columns=['artist', 'venue'], values='concert_count', fill_value=0)
    
    # Flatten multi-level columns to create a single-level column with (artist_venue) pairs
    pivot_table.columns = [f'{artist}_{venue}' for artist, venue in pivot_table.columns]
    
    return pivot_table

def main():
    print("Welcome to the Concert Count Table Generator!")
    
    # Step 1: Get the input data from the user
    df = get_input_data()
    
    # Step 2: Create the concert table
    pivot_table = create_concert_table(df)
    
    # Step 3: Display the resulting table
    print("\nHere is your concert count table:")
    print(pivot_table)

# Run the program
main()
