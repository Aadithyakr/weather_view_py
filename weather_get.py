import requests
import tkinter as tk
from tkinter import messagebox

def get_weather_data(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"

    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather = data['weather'][0]

        weather_info = (
            f"City: {data['name']}\n"
            f"Temperature: {main['temp']}°C\n"
            f"Humidity: {main['humidity']}%\n"
            f"Pressure: {main['pressure']} hPa\n"
            f"Weather: {weather['description'].capitalize()}\n"
            f"Wind Speed: {wind['speed']} m/s"
        )

        return weather_info
    else:
        return f"City '{city_name}' not found or other error occurred. Please try again."

def show_weather():
    city_name = city_entry.get()
    api_key = "66275de618dea93ab0c2233cb90b6e88"
    weather_info = get_weather_data(city_name, api_key)
    messagebox.showinfo("Weather Information", weather_info)

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create a label and entry for the city name
city_label = tk.Label(root, text="Enter City Name:")
city_label.pack(pady=10)

city_entry = tk.Entry(root, width=40)
city_entry.pack(pady=10)

# Create a button to trigger the weather fetch
get_weather_button = tk.Button(root, text="Get Weather", command=show_weather)
get_weather_button.pack(pady=20)

# Run the application
root.mainloop()
