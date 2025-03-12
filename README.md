# Bikeshare Data Explorer 🚲

Analyze bikeshare data from Chicago, New York City, and Washington!

## 📝 Description

This interactive data exploration tool allows you to analyze bikeshare ride data from three major US cities. Users can filter data by month and day of the week, then view various statistical analyses including popular stations, trip durations, and user demographics.

## 🔍 Features

- **City Selection**: Choose from three cities (Chicago, New York City, Washington)
- **Time Filtering**: Filter data by month (January to June) and/or day of the week
- **Data Analysis Options**:
  - View raw data (5 rows at a time)
  - Display statistics on the most frequent travel times
  - View popular stations and routes
  - Review trip duration statistics
  - Analyze bikeshare user demographics

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- pandas
- numpy

### Installation

1. Clone this repository or download the source code
2. Ensure you have the required CSV data files in the same directory:
   - `chicago.csv`
   - `new_york_city.csv`
   - `washington.csv`
3. Install required dependencies:
   ```
   pip install pandas numpy
   ```

### Usage

Run the program by executing:

```
python bikeshare.py
```

Follow the interactive prompts to select:
1. A city to analyze
2. Month filter (specific month or 'all')
3. Day filter (specific day or 'all')
4. Analysis options from the main menu

## 📊 Main Menu Options

### 1. Display Raw Data
- Shows 5 rows of raw data at a time
- Option to continue viewing more rows or return to menu

### 2. Time Statistics
- Most frequent month of travel
- Most frequent day of the week for travel
- Most frequent hour of the day for travel

### 3. Station Statistics
- Most commonly used start station
- Most commonly used end station
- Most common trip (combination of start and end stations)

### 4. Trip Duration Statistics
- Total travel time (in hours)
- Average travel time (in minutes)

### 5. User Statistics
- Breakdown of users by type (Subscriber/Customer)
- Gender distribution
- Age demographics based on birth year:
  - Earliest birth year
  - Most recent birth year
  - Most common birth year

## 🔄 Navigation

- Select options by entering the corresponding number
- Return to the main menu or restart the application as needed
- Type 'help' at city selection to see available options

## Example

Below is a sample interaction with the script:

```
Hello! Let's explore some US bikeshare data!

Which City would you like to view? type 'help' to see your options: 
Chicago

Which Month would you like to filter by? type 'help' to see your options, or 'all' to see all months: 
All

Which day would you like to filter by? Type 'all' for no day filter: 
Monday

How would you like to view your data?
Please enter the option number from the choices below, or type 'restart' to restart:
1: Display raw data
2: Display statistics on the most frequent times of travel
3: Display statistics on the most popular stations and trip
4: Display statistics on the total and average trip duration
5: Display statistics on bikeshare users

2

Calculating The Most Frequent Times of Travel...

Most Frequent Month of travel: June
Most Frequent Day of travel: Monday
Most Frequent Hour of travel: 8:00

This took 0.1 seconds.
----------------------------------------

Please chose an option:
1: Back to main menu
2: restart

1
```

## Code Structure

This script is modular, with functions dedicated to specific tasks:

- `get_filters()`: Prompts the user for city, month, and day inputs.

- `load_data()`: Loads the CSV data and applies the specified filters.

- `main_menu()`: Displays the main menu and processes user selections.

- `show_rows()`: Shows raw data in 5-row increments, with options to continue or stop.

- `time_stats()`: Displays the most frequent travel times.

- `station_stats()`: Identifies popular stations and trips.

- `trip_duration_stats()`: Calculates total and average trip durations.

- `user_stats()`: Displays user demographic data.

- `restart_app()`: Allows restarting the app or returning to the main menu.


## 📁 Data Structure

The program expects CSV files with the following columns:
- `Start Time`
- `End Time`
- `Trip Duration`
- `Start Station`
- `End Station`
- `User Type`
- `Gender` (may not be available in all city datasets)
- `Birth Year` (may not be available in all city datasets)

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for any improvements or additional features!
