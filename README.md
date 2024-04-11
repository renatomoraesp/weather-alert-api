# Weather Alert API

## Problem Statement

The Weather Alert API provides real-time weather information and safety alerts to help users make informed decisions about outdoor activities based on current weather conditions. It does that by integrating with the OpenWeather API.

## Dependencies

You can install the required dependencies by running the following command:

`pip install -r requirements.txt`

## Running the API

To run the Weather Alert API, follow these steps:

1. Clone the repository:

`git clone https://github.com/renatomoraesp/weather-alert-api.git`

2. Navigate to the project directory:

`cd weather-alert-api`

3. Create a `.env` file in the project root directory and add your OpenWeather API key:

`API_KEY=YOUR_API_KEY`

4. Run the application:

`python run.py`

5. The API will be accessible at `http://localhost:5000`.

6. You can access the API endpoints using the following URLs:
- Current Weather: `http://localhost:5000/weather/<city>`
- Weather Forecast: `http://localhost:5000/forecast/<city>`

Replace `<city>` with the name of the city for which you want to retrieve weather information.