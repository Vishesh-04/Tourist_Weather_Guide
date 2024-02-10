import tkinter as tk
from tkinter import messagebox
import requests


# Function to fetch weather data from the API
def get_weather(location, min_temp, max_temp):
    # API_KEY = "bb105451e60b48b483880333240102"  # Replace with your API key
    URL = f"http://api.weatherapi.com/v1/current.json?key=bb105451e60b48b483880333240102&q={location}&aqi=no"

    try:
        response = requests.get(URL)
        data = response.json()
        if response.status_code == 200:
            # Extract relevant information from the response
            weather_description = data['current']['condition']['text']
            temperature = data['current']['temp_c']
            humidity = data['current']['humidity']
            wind_speed = data['current']['wind_mph']
            return f"Weather: {weather_description}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s"
        else:
            return "Failed to fetch weather data. Please try again later."
    except Exception as e:
        return f"An error occurred: {str(e)}"


# Function to handle button click event
def on_submit():
    location = location_entry.get().strip()
    min_temp = min_temp_entry.get().strip()
    max_temp = max_temp_entry.get().strip()

    if location:
        weather_info = get_weather(location, min_temp, max_temp)
        messagebox.showinfo("Weather Info", weather_info)
    else:
        messagebox.showwarning("Warning", "Please enter a location.")


# Create main Tkinter window
root = tk.Tk()
root.title("Weather Chatbot")

# Create and place widgets
label1 = tk.Label(root, text="Enter location:")
label1.grid(row=0, column=0, padx=5, pady=5)

location_entry = tk.Entry(root, width=30)
location_entry.grid(row=0, column=1, padx=5, pady=5)

label2 = tk.Label(root, text="Enter min temperature:")
label2.grid(row=1, column=0, padx=5, pady=5)

min_temp_entry = tk.Entry(root, width=10)
min_temp_entry.grid(row=1, column=1, padx=5, pady=5)

label3 = tk.Label(root, text="Enter max temperature:")
label3.grid(row=2, column=0, padx=5, pady=5)

max_temp_entry = tk.Entry(root, width=10)
max_temp_entry.grid(row=2, column=1, padx=5, pady=5)

submit_button = tk.Button(root, text="Get Weather", command=on_submit)
submit_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Start the Tkinter event loop
root.mainloop()
