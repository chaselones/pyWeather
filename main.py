import requests
import tkinter as tk
from tkinter import messagebox

# Constants
API_KEY = '4844e3db24769244c29ce5f1a377b81e'
API_URL = "http://api.openweathermap.org/data/2.5/weather"

# Function to get weather data from the API
def get_weather(city, api_key):
    url = f"{API_URL}?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    # Debugging: Print the request URL, response status code, and response body
    print(f"URL: {url}")
    print(f"Response Code: {response.status_code}")
    print(f"Response Body: {response.text}")
    
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        messagebox.showerror("Error", f"City '{city}' not found.")
        return None
    else:
        messagebox.showerror("Error", f"API error: {response.status_code}")
        return None

# Function to parse the weather data
def parse_weather_data(data):
    weather = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'description': data['weather'][0]['description']
    }
    return weather

# Function to show weather information in the GUI
def show_weather():
    city = city_entry.get()
    weather_data = get_weather(city, API_KEY)
    if weather_data:
        parsed_data = parse_weather_data(weather_data)
        weather_info = (
            f"City: {parsed_data['city']}\n"
            f"Temperature: {parsed_data['temperature']}°C\n"
            f"Humidity: {parsed_data['humidity']}%\n"
            f"Description: {parsed_data['description']}"
        )
        messagebox.showinfo("Weather", weather_info)

# Set up the GUI
root = tk.Tk()
root.title("Weather Dashboard")

# GUI Components
tk.Label(root, text="Enter city:").grid(row=0)
city_entry = tk.Entry(root)
city_entry.grid(row=0, column=1)
tk.Button(root, text="Get Weather", command=show_weather).grid(row=1, columnspan=2)

# Start the GUI event loop
root.mainloop()
