# Weather App

A command-line weather application built with Python.

## Features

- Accepts a city name from the user
- Retrieves latitude and longitude using the Open-Meteo Geocoding API
- Fetches current weather information
- Displays local time, temperature, and weather condition
- Handles invalid city names and API connection errors

## Technologies Used

- Python
- Requests library
- Open-Meteo API
- JSON

## How to Run

1. Install Python.
2. Install the Requests library:

   ```bash
   python -m pip install requests
   ```

3. Run the application:

   ```bash
   python weather_app.py
   ```
4. Enter a city name when prompted.

## API Provider

Open-Meteo: https://open-meteo.com/

## Learning Outcomes

- Making HTTP GET requests using the Requests library
- Working with APIs and JSON responses
- Passing query parameters to APIs
- Handling connection errors and invalid city names
- Writing reusable Python functions
- Extracting and formatting weather data