import sys
import requests
import json
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, 
                              QPushButton, QVBoxLayout, QWidget, QLineEdit)
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name:", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        
        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.get_weather_button.clicked.connect(self.get_weather)

        # Apply dark theme styles
        self.setStyleSheet("""
            QWidget {
                background-color: white;
                color: black;
                font-size: 14px;
            }
            
            QLabel#city_label {
                padding: 8px;
                border-radius: 4px;
                font-size: 20px;
                font-weight: bold;
            }
            
            QLineEdit#city_input {
                padding: 8px;
                background-color: white;
                border: 1px solid #555555;
                border-radius: 4px;
                font-size: 20px;
                font-weight: bold;
            }
            
            QLineEdit#city_input:hover {
                background-color: #dae6e3;
                border: 1px solid #666666;
            }
            
            QPushButton#get_weather_button {
                padding: 10px;
                background-color: #0d47a1;
                border: none;
                border-radius: 4px;
                color: white;
            }
            
            QPushButton#get_weather_button:hover {
                background-color: #1565c0;
            }
            
            QPushButton#get_weather_button:pressed {
                background-color: #0a3d8f;
            }
            
            QLabel#emoji_label {
                font-size: 48px;
                font-family: segoe ui emoji;
            }
            
            QLabel#temperature_label {
                font-size: 24px;
                font-weight: bold;
            }
            
            QLabel#description_label {
                font-size: 20px;
            }
        """)

    def get_weather(self):
        
        api_key = "ENTER_YOUR_API_KEY"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError:
            match response.status_code:
                case 400:
                    self.display_error("Bad Request:\nPlease check the city name")
                case 401:
                    self.display_error("Unauthorized:\nPlease check your API key")
                case 402:
                    self.display_error("Payment Required:\nPlease check your API key")
                case 403:
                    self.display_error("Forbidden:\nPlease check your API key")
                case 404:
                    self.display_error("City not found:\nPlease check the city name")
                case 429:
                    self.display_error("Rate limit exceeded:\nPlease try again later")
                case 501:
                    self.display_error("Invalid API key:\nPlease check your API key")
                case 500:
                    self.display_error("Internal server error:\nPlease try again later")
                case 502:
                    self.display_error("Bad Gateway:\nPlease try again later")
                case 503:
                    self.display_error("Service Unavailable:\nPlease try again later")
                case 504:
                    self.display_error("Gateway Timeout:\nPlease try again later")
                case 520:
                    self.display_error("Web Server Returned an Unknown Error:\nPlease try again later")
                case 524:
                    self.display_error("A Timeout Occurred:\nPlease try again later")
                case 525:
                    self.display_error("A Timeout Occurred:\nPlease try again later")
                case 526:
                    self.display_error("Invalid SSL Certificate:\nPlease check your API key")
                case 527:
                    self.display_error("Railgun Error:\nPlease try again later")
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nPlease check your internet connection")

        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request took too long to complete")

        except requests.exceptions.TooManyRedirects:
            self.display_error("Too Many Redirects:\nPlease check the URL")

        except requests.exceptions.JSONDecodeError:
            self.display_error("JSON Decode Error:\nPlease check the data format")

        except requests.exceptions.RequestException:
            self.display_error("An error occurred while making the request")
            


    def display_error(self, message):
        self.temperature_label.setStyleSheet("color: red; font-size: 30px")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, weather_data):
        self.temperature_label.setStyleSheet("color: black; font-size: 30px")
        ##To extract the temperature value;
        temperature_k = weather_data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        temperature_f = (temperature_k - 273.15) * 9/5 + 32
        weather_id = weather_data["weather"][0]["id"]
        weather_description = weather_data["weather"][0]["description"]

        self.temperature_label.setText(f"Temperature is {temperature_c:.2f}°C")
        self.description_label.setText(f"Weather is {weather_description}")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))

        #print(weather_data)

    @staticmethod
    def get_weather_emoji(weather_id):
        # Clear sky
        if weather_id == 800:
            return "☀️"  # Clear sky
        elif weather_id == 801:
            return "🌤️"  # Few clouds
        elif weather_id == 802:
            return "⛅"  # Scattered clouds
        elif weather_id == 803:
            return "🌥️"  # Broken clouds
        elif weather_id == 804:
            return "☁️"  # Overcast clouds
        # Thunderstorm
        elif weather_id >= 200 and weather_id <= 202:
            return "⛈️"  # Thunderstorm with rain
        elif weather_id >= 210 and weather_id <= 221:
            return "🌩️"  # Thunderstorm
        elif weather_id >= 230 and weather_id <= 232:
            return "⛈️"  # Thunderstorm with drizzle
        # Drizzle
        elif weather_id >= 300 and weather_id <= 321:
            return "🌦️"  # Drizzle
        # Rain
        elif weather_id >= 500 and weather_id <= 504:
            return "🌧️"  # Rain
        elif weather_id == 511:
            return "🌨️"  # Freezing rain
        elif weather_id >= 520 and weather_id <= 531:
            return "🌧️"  # Shower rain
        # Snow
        elif weather_id >= 600 and weather_id <= 602:
            return "🌨️"  # Snow
        elif weather_id >= 611 and weather_id <= 616:
            return "🌨️"  # Sleet
        elif weather_id >= 620 and weather_id <= 622:
            return "🌨️"  # Shower snow
        # Atmosphere
        elif weather_id == 701:
            return "🌫️"  # Mist
        elif weather_id == 711:
            return "💨"  # Smoke
        elif weather_id == 721:
            return "🌫️"  # Haze
        elif weather_id == 731 or weather_id == 761:
            return "🌪️"  # Dust/Sand whirls
        elif weather_id == 741:
            return "🌫️"  # Fog
        elif weather_id == 751:
            return "🌪️"  # Sand
        elif weather_id == 762:
            return "🌋"  # Volcanic ash
        elif weather_id == 771:
            return "💨"  # Squalls
        elif weather_id == 781:
            return "🌪️"  # Tornado
        if weather_id >= 200 and weather_id < 232:
            return "🌩️"
        elif weather_id >= 300 and weather_id < 321:
            return "🌧️"
        elif weather_id >= 500 and weather_id < 531:
            return "🌧️" #
        elif weather_id >= 600 and weather_id < 622:
            return "❄️"  # Snow conditions (600-622 range represents various types of snow)
        elif weather_id >= 700 and weather_id < 781:
            return "🌫️"  # Fog conditions (700-781 range represents various types of fog)
        elif weather_id >= 800 and weather_id < 804:
            return "☀️"  # Clear sky conditions (800-804 range represents various types of clear sky)
        else:
            return "🌈"  # Default emoji for unknown weather conditions
        
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())