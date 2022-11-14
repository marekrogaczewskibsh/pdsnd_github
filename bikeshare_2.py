import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

POSSIBLE_ANSWERS = ['month', 'day', 'both', 'not at all']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    city = ''
    city_question = 'Would you like to see data for Chicago, New York, or Washington? '

    while city not in CITY_DATA:
        city = input(city_question).lower()

    # get user input for month (all, january, february, ... , june)
    month = 'all'
    filter_question = 'Would you like to filter the data by "month", "day", "both" or "not at all"? '
    user_filter = ''

    while user_filter not in POSSIBLE_ANSWERS:
        user_filter = input(filter_question).lower()

    if user_filter in ['month', 'both']:
        month_question = 'Which month - January, February, March, April, May, or June? '
        month = ''

        while month not in MONTHS:
            month = input(month_question).lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = 'all'

    if user_filter in ['day', 'both']:
        day_question = 'Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? '
        day = ''

        while day not in DAYS:
            day = input(day_question).lower()

    print(f'\nPreparing data for: \n\tcity \t- {city.title()}\n\tmonth \t- {month.title()}\n\tday \t- {day.title()}')


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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = MONTHS.index(month)

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
    common_month = df['month'].mode()[0]
    print(f'The most common month: {MONTHS[common_month].title()}')

    # display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print(f'The most common day of week: {common_day_of_week}')

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(f'The most common start hour: {popular_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    count_start_station = df['Start Station'].value_counts()[0]
    print(f'The most common Start Station: {common_start_station}, count: {count_start_station}')

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    count_end_station = df['End Station'].value_counts()[0]
    print(f'The most common End Station: {common_end_station}, count: {count_end_station}')

    # display most frequent combination of start station and end station trip
    df_frequent_start = df[df['Start Station'] == common_start_station]
    frequent_end = df_frequent_start['End Station'].mode()[0]
    count_frequent_trip = df_frequent_start['End Station'].value_counts()[0]
    print(f'The most frequent trip is from {common_start_station} to {frequent_end}, count: {count_frequent_trip}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
