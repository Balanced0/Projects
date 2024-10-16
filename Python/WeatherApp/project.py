import requests
from tkinter import *
from tkinter import messagebox
def main():
    app = Tk()
    app.title("Weather App")
    app.geometry("700x350")

    global city_text
    city_text = StringVar()
    city = Entry(app, textvariable = city_text)
    city.pack()

    search_bt = Button(app, text="Search Weather", width="12", command = search)
    search_bt.pack()

    global location_lbl
    location_lbl = Label(app, text="", font=("bold", 20))
    location_lbl.pack()

    global img_lbl
    img_lbl = Label(app)
    img_lbl.pack()

    global temp_lbl
    temp_lbl = Label(app, text="")
    temp_lbl.pack()

    global weather_lbl
    weather_lbl = Label(app, text="")
    weather_lbl.pack()
    app.mainloop()




def get_weather(city):
    api_key = "c0d53d335f6590d3071a33ba632b4270"
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}")
    if weather_data:
        json = weather_data.json()
        city = json["name"]
        country = json["sys"]["country"]
        temp_cel = json["main"]["temp"]
        icon = json["weather"][0]["icon"]
        weather = json["weather"][0]["main"]
        final = (city, country, temp_cel, icon, weather)
        return final
    else:
        return None

def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_lbl["text"] = "{}, {}".format(weather[0], weather[1])
        img = PhotoImage(file=f"weather_icons/{weather[3]}.png")
        img_lbl.config(image=img)
        img_lbl.image = img 
        temp_lbl["text"] = "{:.2f}°C".format(weather[2])
        weather_lbl["text"] = "{}".format(weather[4])
        
    else:
        messagebox.showerror("Error", "Cannot find city {}".format(city))


def reset():
    city_text.set("") 
    location_lbl.config(text="")
    img_lbl.config(image="")
    temp_lbl.config(text="")
    weather_lbl.config(text="")


if __name__ == "__main__":
    main()