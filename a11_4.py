import pandas as pd

# Step 1: Take input for the schedule
days = []
visits = []


n=int(input("enter no. of schedules u want to enter:-"))
print(f"Enter the schedule for the next {n} days:")
for i in range(n):
    day = input(f"Enter the date for day {i + 1} (e.g., 2025-04-10): ")
    visit = input(f"Is John and Judy visiting on {day}? (yes/no): ").strip().lower()
    
    days.append(day)
    visits.append(True if visit == 'yes' else False)

# Step 2: Create the DataFrame
df = pd.DataFrame({
    'day': days,
    'john_judy_visiting': visits
})

# Step 3: Create the 'days_til_party' column
df['days_til_party'] = None

# Step 4: Iterate backwards through the DataFrame to fill the 'days_til_party' column
party_day = None
for i in range(len(df)-1, -1, -1):
    if df.loc[i, 'john_judy_visiting']:  # A party happens on this day
        party_day = i
        df.loc[i, 'days_til_party'] = 0
    elif party_day is not None:
        df.loc[i, 'days_til_party'] = party_day - i

# Step 5: Display the result
print("\nSchedule with 'days_til_party':")
print(df)
