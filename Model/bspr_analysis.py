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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please enter the name of the city you want data for: Chicago, New York City, Washington        ')

    # get user input for month (all, january, february, ... , june)
    month = input('Please enter the name of the month you want data for: january, february, march, april, may, june or all       ')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please enter the day of the week you want data for: sunday, monday, tuesday, wednesday, thursday, friday, saturday or all        ')

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
    if city.lower() == 'chicago':
        df = pd.read_csv('chicago.csv')
    elif city.lower() == 'new york city' or city.lower() =='new york':
        df = pd.read_csv('new_york_city.csv')
    elif city.lower() == 'washington':
        df = pd.read_csv('washington.csv')
    else :
        print('Please enter a valid city name: Chicago, New York City or Washington')

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month.lower() != 'all'  :
        try:
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month = months.index(month) + 1
            df = df[df['month'] == month]
        except:
            print('Please enter a valid month name: january, february, march, april, may or june in lowercase')
    if day.lower() != 'all' :
        df = df[df['day_of_week'] == day.title()]


    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['hour'] = df['Start Time'].dt.hour
    # display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Common month is {}'.format(popular_month))

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Common day is {}'.format(popular_day))

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common hour is {}'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Commonly used start station is {}'.format(popular_start_station))

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Commonly used end station is {}'.format(popular_end_station))

    # display most frequent combination of start station and end station trip
    frequent_stations = df.groupby(['Start Station','End Station']).size().nlargest(1)
    print('Most frequent combination of start station and end station trip is {} '.format(frequent_stations))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    Total_travel_time = df['Trip Duration'].sum()
    print('Total Travel time is {}'.format(Total_travel_time))
    # display mean travel time
    Mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel time is {}'.format(Mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Type count is {}'.format(user_types))

    # Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('Gender count is {}'.format(gender_count))
    except:
        print('Gender not defined')

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_by = df['Birth Year'].min()
        print('Earliest year of birth is {}'.format(earliest_by))
        recent_by = df['Birth Year'].max()
        print('Most recent year of birth is {}'.format(recent_by))
        common_by = df['Birth Year'].mode()
        print('Most common year of birth is {}'.format(common_by))
        print("\nThis took %s seconds." % (time.time() - start_time))
    except:
        print('Birth Year not defined')
    print('-'*40)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    raw_data_disp = input('\nWould you like to see raw data? Enter yes or no.\n')
    count = 5
    if raw_data_disp.lower() != 'yes':
        return
    else:
        print(df.head(5))

    while True:
        more_data = input('\nWould you like to see 5 more rows of raw data? Enter yes or no.\n')
        if more_data.lower() != 'yes':
            break
        else:
            print(df.iloc[count:count+5])
            count = count+5



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
