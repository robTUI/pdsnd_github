import time
import pandas as pd
import numpy as np

# Set the display option to show all columns
pd.set_option('display.max_columns', None)
# Set the display format for floats to one decimal place
pd.options.display.float_format = '{:.1f}'.format

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
available_months = ['January', 'February', 'March', 'April', 'May', 'June']
days =  ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n This interactive data exploration tool allows you to analyze bikeshare ride data from three major US cities.\n Filter data by month and day of the week, then view various statistical analyses including popular stations, trip durations, and user demographics.' )
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nWhich City would you like to view? type 'help' to see your options: \n").title()
        if city == 'Help':
            print("\nyour options are:\nChicago | Washington | New York City\n")
        elif city.lower() in CITY_DATA:
            print(f"\nloading data for {city}...\n")
            break
        else:
            print("\nCity not found, type 'help' to see your options!\n")
    # get user input for month (all, january, february, ... , june)
    while True:        
        month = input("\nWhich Month would you like to filter by? We have date for January to June.\n type 'help' to see your options, or 'all' to see all months: \n").title()
        if month == 'Help':
            print("\nyour options are:\nJanuary | February | March | April | May | June\n")
        elif month == 'All':
            print("\nloading data for all available months\n")
            break
        elif month in available_months:
            print(f"\nloading data for {month}...\n")
            month = available_months.index(month) + 1
            break
        else:
            print("\nMonth not found! Please check your spelling is correct or type 'help' to see your options!\n")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nWhich day would you like to filter by? Type 'all' for no day filter: \n").title()
        if day in days:
            print(f'\nLoading data for {day}\n')
            break
        elif day == 'All':
            print('\nLoading all days\n')
            break
        else:
            print('\nDay not found, please check your spelling!\n')

    print('-'*40)
    
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load file
    df = pd.read_csv(CITY_DATA[city.lower()])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month from & day of week from Start Time col & create new columns for month & day
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    
    if month != 'All':
        # filter by Month to create the new dataframe
        df = df[df['month'] == month]
        
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    
    return df

def main_menu(df):    
    while True:
        option = input(
"""
How would you like to view your data?
Please enter the option number from the choices below, or type 'restart' to restart:
1: Display raw data
2: Display statistics on the most frequent times of travel
3: Display statistics on the most popular stations and trip
4: Display statistics on the total and average trip duration
5: Display statistics on bikeshare users
""")
        if option == '1':
            show_rows(df)
        elif option == '2':
            time_stats(df)
        elif option == '3':
            station_stats(df)
        elif option == '4':
            trip_duration_stats(df)
        elif option == '5':
            user_stats(df)
        elif option == 'restart':
            main()
        else:
            print("Error: Command not recognised, please try again")

def restart_app(df):
    """
    Restarts app or returns to main menu
    """
    while True:
        option = input("""
Please chose an option:
1: Back to main menu
2: restart
""")
        if option == '1':
            main_menu(df)
        elif option == '2':
            main()
        else:
            print('Error: Command not recognised, please try again')
            
def show_rows(df):
    """
    Reveals 5 rows of the raw data on user input
    """
    while True:
        total_rows = len(df)
        chunk_size = 5
        start_row = 0
        
        while start_row < total_rows:
            end_row = start_row + chunk_size
            print(f"\nDisplaying rows {start_row} to {end_row}...\n")
            print(df.iloc[start_row:end_row]) # show 5 rows

            start_row += chunk_size # next start row
            
            # check if there are more rows left
            if start_row < total_rows:
                user_input = input("\nPress Enter to show 5 more rows, or type 'stop' to stop...\n")
                if user_input.lower() == "stop":
                    print("\nExiting...\n")
                    restart_app(df)

        if start_row >= total_rows:
            print("\nNo more rows to display.\n")
            restart_app(df)

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # display the most common month
    df['month'] = df['Start Time'].dt.month_name()
    top_month = df['month'].mode()[0]
    
    # display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.day_name()
    top_day = df['day_of_week'].mode()[0]
    

    # display the most common start hour
    top_hour = df['Start Time'].dt.hour.mode()[0]    

    
    print(f"\nMost Frequent Month of travel: {top_month}\n")
    print(f"Most Frequent Day of travel: {top_day}\n")
    print(f"Most Frequent Hour of travel: {top_hour}:00\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    restart_app(df)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    top_start_station = df['Start Station'].mode()[0]
    

    # display most commonly used end station
    top_end_station = df['End Station'].mode()[0]
    

    # display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + " to " + df['End Station']
    most_frequent_trip = df['Trip'].mode()[0]

    print(f"\nMost Commonly Used Start Station: {top_start_station}\n")
    print(f"Most Commonly Used End Station: {top_end_station}\n")
    print(f"Most Frequent Trip: {most_frequent_trip}\n")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    restart_app(df)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_travel_time_hours = round(total_travel_time / 3600, 1)    

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_travel_time_minutes = round(mean_travel_time / 60, 1)

    print(f"\nTotal travel time: {total_travel_time_hours} hours\n")
    print(f"Average travel time: {mean_travel_time_minutes} minutes\n")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    restart_app(df)
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()    

    # Display counts of gender
    gender_count = df['Gender'].value_counts()    

    # Display earliest, most recent, and most common year of birth
    earliest_user_dob = int(df['Birth Year'].min())
    latest_user_dob = int(df['Birth Year'].max())
    most_common_dob = int(df['Birth Year'].mode()[0])

    print(f"\nCount of users by type: \n{user_types.to_string(index=True)}")
    print(f"\nCount of users by gender: \n{gender_count.to_string(index=True)}")
    print(f"\nEarliest user date of birth: {earliest_user_dob}")
    print(f"\nLatest user date of birth: {latest_user_dob}")
    print(f"\nMost common date of birth: {most_common_dob}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    restart_app(df)
    
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        main_menu(df)

if __name__ == "__main__":
	main()
