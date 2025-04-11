# Weather API Project

A simple weather API service built with FastMCP that provides weather alerts and forecasts using the National Weather Service (NWS) API.

## Features

- Get weather alerts for any US state
- Get detailed weather forecasts for specific locations
- Built with FastMCP for easy integration
- Uses the official National Weather Service API

## Installation

1. Clone the repository:
```bash
git clone https://github.com/shaibs3/weather.git
cd weather
```

2. Install dependencies:
```bash
uv pip install -r requirements.txt
```

## Usage

Run the server:
```bash
python main.py
```

### Available Endpoints

1. Get Weather Alerts
   - Input: US state code (e.g., "CA", "NY")
   - Returns: Active weather alerts for the specified state

2. Get Weather Forecast
   - Input: Latitude and longitude coordinates
   - Returns: Detailed weather forecast for the specified location

## API Documentation

The service uses the National Weather Service API to provide accurate and up-to-date weather information.

## License

This project is open source and available under the MIT License.
