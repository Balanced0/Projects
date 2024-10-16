
# Weather App
#### Video Demo:  https://youtu.be/_SXsNWXwvR4
#### Description:
This is a simple weather app project that uses Python and the Tkinter library to show the weather of any city that the user searches for. It uses the OpenWeatherMap API to get weather data like temperature, weather conditions, and more.

## Code Explanation

Below is a step-by-step explanation of how the code works.

### 1. Importing the Necessary Libraries

```python
import requests
from tkinter import *
from tkinter import messagebox
```

- `requests`: This library helps us send requests to APIs and get data from them.
- `tkinter`: This is used to create the graphical interface of the app (the windows, buttons, labels, etc.).
- `messagebox`: A part of Tkinter, it helps us display error messages.

### 2. Main Function to Build the App Window

```python
def main():
    app = Tk()
    app.title("Weather App")
    app.geometry("700x350")
```
- `Tk()` creates the main app window.
- We set the title to "Weather App" and the window size to 700x350.

#### Adding Widgets (Entry, Button, Labels)
```python
global city_text
city_text = StringVar()
city = Entry(app, textvariable = city_text)
city.pack()
```
- `city_text` is used to store the input city name.
- We use an `Entry` widget to let users type in the city name.

```python
search_bt = Button(app, text="Search Weather", width="12", command = search)
search_bt.pack()
```
- A search button is created that runs the `search` function when clicked.

```python
global location_lbl, img_lbl, temp_lbl, weather_lbl
location_lbl = Label(app, text="", font=("bold", 20))
location_lbl.pack()
img_lbl = Label(app)
img_lbl.pack()
temp_lbl = Label(app, text="")
temp_lbl.pack()
weather_lbl = Label(app, text="")
weather_lbl.pack()
```
- These labels are used to display the location, temperature, weather icon, and weather condition after the user searches.

Finally, we start the app using `app.mainloop()`.

### 3. Fetching Weather Data from OpenWeatherMap API

```python
def get_weather(city):
    api_key = "c0d53d335f6590d3071a33ba632b4270"
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}")
```
- This function sends a request to the OpenWeatherMap API to get weather details.
- If the data is found, it returns a tuple with the city name, country, temperature, icon ID, and weather type.

### 4. Search Function to Show Weather Data

```python
def search():
    city = city_text.get()
    weather = get_weather(city)
```
- The `search` function gets the city from the input and calls `get_weather()` to get weather data.

If data is found, it updates the labels and loads an icon:
```python
img = PhotoImage(file=f"weather_icons/{weather[3]}.png")
img_lbl.config(image=img)
img_lbl.image = img 
temp_lbl["text"] = "{:.2f}°C".format(weather[2])
weather_lbl["text"] = "{}".format(weather[4])
```
- If the city is not found, an error message is shown using `messagebox.showerror()`.

### 5. Reset Function

```python
def reset():
    city_text.set("") 
    location_lbl.config(text="")
    img_lbl.config(image="")
    temp_lbl.config(text="")
    weather_lbl.config(text="")
```
- This function resets the input and clears the labels.

### 6. Running the App

```python
if __name__ == "__main__":
    main()
```
- This part makes sure the app runs only if the file is executed directly and not imported.

## How the App Works
1. Type a city name in the input field.
2. Click the "Search Weather" button.
3. The weather information for that city will be displayed if found.
4. If the city is not found, you will get an error message.

This is a very simple app that gives you a good starting point to learn about APIs and GUI development with Tkinter.
