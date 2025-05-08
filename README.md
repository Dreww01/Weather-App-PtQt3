# Weather App

A modern desktop weather application built with Python and PyQt5 that provides real-time weather information for any city worldwide.

## Features

- **Real-time Weather Data**
  - Current temperature in Celsius
  - Weather condition descriptions
  - Visual weather representation using emojis
  - Location-based weather information

- **User Interface**
  - Clean, modern design with dark theme
  - Responsive layout
  - User-friendly input system
  - Centered text alignment for better readability
  - Custom styling for all UI elements

- **Error Handling**
  - Comprehensive error messages for various scenarios:
    - Invalid city names
    - Network connectivity issues
    - API rate limiting
    - Server errors
    - Invalid API keys
    - Timeout handling

## Requirements

- Python 3.x
- PyQt5
- requests library
- Internet connection

## Installation

1. Install the required dependencies:
   ```bash
   pip install PyQt5 requests
   ```

2. Clone or download the repository

3. Run the application:
   ```bash
   python WEATHER-APP-PYQT5.PY
   ```

## Usage

1. Launch the application
2. Enter a city name in the input field
3. Click the "Get Weather" button
4. View the current weather information including:
   - Temperature in Celsius
   - Weather description
   - Visual weather emoji

## Technical Details

### API Integration
- Uses OpenWeatherMap API
- Handles various HTTP status codes
- Implements proper error handling for API responses

### Weather Emoji System
The app includes a comprehensive weather emoji system that displays appropriate emojis based on weather conditions:
- ☀️ Clear sky
- 🌤️ Few clouds
- ⛅ Scattered clouds
- 🌥️ Broken clouds
- ☁️ Overcast clouds
- ⛈️ Thunderstorm
- 🌦️ Drizzle
- 🌧️ Rain
- 🌨️ Snow
- 🌫️ Mist/Fog
- And many more...

### UI Components
- Custom styled QLineEdit for city input
- Styled QPushButton for weather retrieval
- Multiple QLabels for displaying weather information
- Responsive QVBoxLayout for proper component arrangement

## Error Messages

The application provides detailed error messages for various scenarios:
- Network connectivity issues
- Invalid city names
- API key problems
- Server errors
- Rate limiting
- Timeout issues

## Contributing

Feel free to contribute to this project by:
1. Forking the repository
2. Creating a new branch
3. Making your changes
4. Submitting a pull request

## License

This project is open source and available under the MIT License.

## Note

Make sure you have a stable internet connection to use this application, as it requires real-time API calls to fetch weather data. 
