'''prepared by kareem ayman abdella
the first project in udacity and fwd (bikeshare)'''
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Enter city from those to explore some US bikeshare data (chicago, new york city or washington) \n").lower()
        if city in CITY_DATA:
            break
        else:
            print("please enter chicago, new york city or washington in lowercase")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter month from those to explore some US bikeshare data (january, february, march, april, may, june or all) '\n'").lower()
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
        if month in months:
            break
        else:
            print("please enter correct month in lowercase")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter day from those to explore some US bikeshare data (monday, tuesday, wednesday, thursday, friday, saturday, sunday or all) '\n'").lower()
        days = ['monday', 'tuesday', 'wednesday', 'april', 'thursday', 'friday', 'saturday', 'sunday', 'all']
        if day in days:
            break
        else:
            print("please enter correct day in lowercase")

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
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week, hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]

    print('Most Popular Month: ', most_common_month)

    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]

    print('Most Day Of Week: ', most_common_day_of_week)

    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]

    print('Most Common Start Hour: ', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_commonly_used_start_station = df['Start Station'].mode()[0]

    print('Most Start Station:', most_commonly_used_start_station)

    # TO DO: display most commonly used end station
    most_commonly_used_end_station = df['End Station'].mode()[0]

    print('Most End Station:', most_commonly_used_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    group_field=df.groupby(['Start Station','End Station'])
    most_combination_station = group_field.size().sort_values(ascending=False).head(1)
    print('Most frequent combination of Start Station and End Station trip:\n', most_combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print('Mean Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('User Type Stats:')
    print(df['User Type'].value_counts())
    
    # TO DO: Display counts of gender
    try:
        print('Gender Stats:')
        print(df['Gender'].value_counts())
    except:
        print("There is no 'Gender'  in this station.")

    try:
        earliest_year = int(df['Birth Year'].min())
        print("The earliest year of birth: ",earliest_year)
        most_recent_year = int(df['Birth Year'].max())
        print("The most recent year of birth: ",most_recent_year)
        most_common_year = int(df['Birth Year'].mode()[0])
        print("The most common year of birth: ",most_common_year)
    except:
        print("There is no details about Birth date in this station.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Function to display the row data frame as per user request
def display_data(df):
    """Displays 5 rows of row data from the csv file for the selected city.

    Arguments:
        param1 (df): The data frame you wish to work with.

    Returns:
        None.
    """
    User_Response = ['yes', 'no']
    Row_Data = ''
    #start_loc variable is initialized as a tag to ensure only details from
    #a particular point is displayed
    start_loc = 0
    while Row_Data not in User_Response:
        print("\nWould you like to view 5 rows of individual trip data? Enter yes or no")
        Row_Data = input().lower()
        #the raw data from the df is displayed if user choose it
        if Row_Data == "yes":
            print(df.head(5))
        elif Row_Data not in User_Response:
            print("\nPlease choose yes or no in lowercase")
            print("\nRestarting...\n")

    #while loop for asking user if they want to continue or not.
    while Row_Data == 'yes':
        print("Do you wish to continue?: ")
        start_loc += 5
        Row_Data = input().lower()
        #If user write yse , this displays next 5 rows of data
        if Row_Data == "yes":
             print(df[start_loc:start_loc+5])
        elif Row_Data != "yes":
             break

    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


