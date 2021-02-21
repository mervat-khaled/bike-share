import pandas as pd
import numpy as np 
import time 

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
          
def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city =input('Would you like to see data for Chicago, New York, or Washington?').strip().lower()
        if city not in ("chicago","new york","washington"):
            print("Yourinput should be: Chicago, New York, or Washington?")
            continue
        else:
            break  
    while True:
        month=input('Which month - January, February, March, April, May, June, or all?\n HINT: Enter yourinput without space').lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june','all'):
            print("Yourinput should be: January, February, March, April, May, June, or all")
            continue   
        else:
            break
    while True:

        day=input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all?\nHINT: Enter yourinput without space ').lower()
        if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all'):
                print("Yourinput should be: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all")
                continue
        else:
            break
    return city, month, day

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = df['month'].mode()[0]
    print(f'The most common month is: {months[month-1]}')

    day = df['day_of_week'].mode()[0]
    print(f'The most common day of week is: {day}')

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(f'The most common start hour is: {popular_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    popular_start_station = df['Start Station'].mode()[0]
    print(f'The most popular start station is: {popular_start_station}')

    popular_end_station = df['End Station'].mode()[0]
    print(f'The most popular end station is: {popular_end_station}')

    popular_trip = df['Start Station'] + ' to ' + df['End Station']
    print(f'The most popular trip is: from {popular_trip.mode()[0]}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_duration = round(np.sum(df["Trip Duration"]))//60
    print(f'Total travel time is: {total_travel_duration} minutes')

    average_travel_duration = round(np.mean(df["Trip Duration"])//60)
    print(f'Average travel time is: {average_travel_duration} minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print(df['User Type'].value_counts().to_frame())
    print('\n\n')

    if 'Gender' in(df.columns):
        print(df['Gender'].value_counts().to_frame())
        print('\n\n')

    if 'Birth Year' in(df.columns):
        year = df['Birth Year']
        print(f'Earliest birth year is: {year.min():.0f}\nmost recent is: {year.max():.0f}\nand most comon birth year is: {year.mode()[0]:.0f}')
        print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Ask the user if he wants to display the raw data and print 5 rows at time"""
    raw = input('\nWould you like to diplay raw data?\n Enter yes or no').strip()
    if raw.lower() == 'yes':
        count = 0
        while True:
            print(df.iloc[count: count+5])
            count += 5
            ask = input('Next 5 raws?')
            if ask.lower() != 'yes':
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').strip()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
    