import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


# get user input for month (all, january, february, ... , june)
def filter_by_month():
    while True:
        try:
            month = input("Which month? January, February, March, April, May or June?\n")
            break
        except:
            print('Please Enter a valid name of a month !\n')
            continue
    return month

# get user input for day of week (all, monday, tuesday, ... sunday)
def filter_by_day():
    while True:
        try:
            day = input("Which day? Sunday, Monday, Tuesday, ..... Saturday?\n")
            break
        except:
            print('Please Enter a valid name of a day !\n')
            continue
    return day

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')


    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        try:
            city = input("Whould you like to see data for chicago, new_york_city or washington?\n")
            city = city.lower()
            break
        except:
            print('Please Enter a valid name of a city !\n')
            continue

    filtering = input("Whould you like to filter the data with month, day, both or not at all? Type 'none' for no time filter.\n")

    if filtering == "both":
        month = filter_by_month()
        day = filter_by_day()
    elif filtering == "month":
        month = filter_by_month()
        day = "all"
    elif filtering == "day":
        month = "all"
        day = filter_by_day()
    elif filtering == "none":
        month = "all"
        day = "all"
    print('-' * 40)
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

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
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

    # display the most common month

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month
    # find the most common month
    popular_month = df['month'].mode()[0]
    print('Most Frequent Month:', popular_month)

    # display the most common day of week

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract day from the Start Time column to create a day column
    df['day'] = df['Start Time'].dt.weekday_name
    # find the most common day
    popular_day = df['day'].mode()[0]
    print('Most Frequent Day:', popular_day)

    # display the most common start hour

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    # find the most common Start Station
    most_start_station = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station:', most_start_station)


    # display most commonly used end station

    # find the most common end Station
    most_end_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station:', most_end_station)

########################################################################################
    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    # find the sum of total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)

    # display mean travel time

    # find the mean of total travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    # print value counts for each user type
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender

    # print value counts for each user gender
    user_genders = df['Gender'].value_counts()
    print(user_genders)

    # Display earliest, most recent, and most common year of birth
    earliest_birth_year = df['Birth Year'].min()
    print('Earliest Birth Year:', earliest_birth_year)

    recent_birth_year = df['Birth Year'].max()
    print('Most Recent Birth Year:', recent_birth_year)

    common_birth_year = df['Birth Year'].mode()
    print('Most common Birth Year:', common_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city != "washington":
            user_stats(df)

        raw = input("\nWould you like to see some row data about the bike sharing system in the city?\nEnter yes or no.\n")
        if raw.lower() != 'yes':
            continue

        else:
            counter = 5
            while True:
                print(df.head(counter))
                counter += 5
                raw_again = input(
                    "\nWould you like to see 5 more rows data about the bike sharing system in the city?\nEnter yes or no.\n")
                if raw_again.lower() != 'yes':
                    break


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
