import requests
import time
from tkinter import *
from tkinter import ttk

API_KEY = "8425094d1c19b9ab025d2d13476cbf1b"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
root = Tk()


def convert_time(unix_time):
    converted_date = time.strftime('%H:%M', time.localtime(unix_time))  # Convert UNIX time data to human readable Time.
    return converted_date


def display_weather(e=None) -> None:

    # Clears current displayed weather info
    for widget in frame.winfo_children():
        widget.destroy()

    # Get User Input and clear Entry box
    city = user_input.get()
    user_input.delete(0, len(city))

    # Build request url
    request_url = f"{BASE_URL}?appid={API_KEY}&q={city}&units=metric"

    response = requests.get(request_url)
    # Check to see if request was successful and process data to readable format
    # to display on labels else give Error message.
    if response.status_code == 200:
        data = response.json()
        print(data)
        current_temp = round(data['main']['temp'], 2)
        min_temp = round(data['main']['temp_min'], 2)
        max_temp = round(data['main']['temp_max'], 2)
        temp_real_feel = round(data['main']['feels_like'], 2)
        sunrise_time = convert_time(data['sys']['sunrise'])
        sunset_time = convert_time(data['sys']['sunset'])

        weather_label = Label(frame, text=f"Current weather in {data['name']}, {data['sys']['country']} : "
                                          f"{data['weather'][0]['description']}")
        weather_label.pack()
        temp_label = Label(frame, text=f"Temperature(Celsius):")
        temp_label.pack()
        temp_rf_label = Label(frame, text=f"Current {current_temp}\t Feels like: "
                                          f"{temp_real_feel}\t min: {min_temp}\t max: {max_temp}")
        temp_rf_label.pack()
        sunrise_label = Label(frame, text=f"Sunrise time: {sunrise_time}")
        sunrise_label.pack()
        sunset_label = Label(frame, text=f"Sunset time: {sunset_time}")
        sunset_label.pack()

    else:
        error_label = Label(frame, text="Error occurred")
        error_label.pack()


# Build Gui with Tkinter module
canvas = Canvas(root, width=450, height=150, bg='#00ffff')
canvas.pack()

frame = Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.5, relx=0.1, rely=0.05)

input_label = Label(root, text="Enter the name of a city:")
input_label.pack()
user_input = Entry(root, width=20)
user_input.focus_set()
user_input.pack()

check_weather = Button(root, text="Check Weather", padx=10, pady=5, fg="white", bg="grey", command=display_weather)
check_weather.pack()
root.bind('<Return>', display_weather)

quit_program = Button(root, text="Quit", padx=10, pady=5, fg="white", bg="grey", command=root.destroy)
quit_program.pack()

root.mainloop()
