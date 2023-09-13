import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from datetime import datetime
import pytz

def getweather():
    city = textfield.get()

    # API Key for Weather API
    api_key = "072320f1673e4b9d96d95629231309"

    api = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    response = requests.get(api)
    json_data = response.json()

    if "error" in json_data:
        messagebox.showerror("Error", json_data["error"]["message"])
        return

    condition = json_data['current']['condition']['text']
    temp = json_data['current']['temp_c']
    pressure = json_data['current']['pressure_mb']
    humidity = json_data['current']['humidity']
    wind_speed = json_data['current']['wind_kph']
    timezone = json_data['location']['tz_id']

    local_timezone = pytz.timezone(timezone)
    local_time = datetime.now(local_timezone).strftime("%I:%M %p")

    t.config(text=f"{temp}°")
    c.config(text=f"{condition} | FEELS LIKE {temp}°")
    w.config(text=f"WIND: {wind_speed} km/h")
    h.config(text=f"HUMIDITY: {humidity}%")
    d.config(text=f"DESCRIPTION: {condition}")
    p.config(text=f"PRESSURE: {pressure} hPa")
    name.config(text=f"CURRENT WEATHER IN {city.upper()} ({timezone})")
    clock.config(text=local_time)

root = tk.Tk()
root.title("Weather App")
root.geometry("1200x700+200+100")
root.resizable(False, False)

# App logo
Logo = Image.open("Weather-logo.png")
new_size = (300, 300)
resized_logo = Logo.resize(new_size)
resized_photo = ImageTk.PhotoImage(resized_logo)
resized_logo_label = tk.Label(root, image=resized_photo)
resized_logo_label.place(x=90, y=180)  

# # App Search box
search_image = Image.open("search.png")
search_photo = ImageTk.PhotoImage(search_image)
search_label = tk.Label(root, image=search_photo)
search_label.pack()

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

new_size = (40, 38)
resized_search_image = search_image.resize(new_size)
search_photo = ImageTk.PhotoImage(resized_search_image)
search_icon = Image.open("search_icon.png")  
search_icon = search_icon.resize(new_size)
search_icon_photo = ImageTk.PhotoImage(search_icon)

search_button = tk.Button(root, image=search_icon_photo, borderwidth=0, cursor="hand2", bg="#404040", command=getweather)
search_button.place(x=350, y=40)

# App Bottom box
Frame_image = Image.open("box.png")
frame_photo = ImageTk.PhotoImage(Frame_image)
frame_myimage = tk.Label(root, image=frame_photo)
frame_myimage.pack(padx=5, pady=5, side=tk.BOTTOM)

# Time
name = tk.Label(root, font=("arial",15, "bold"))
name.place(x=30,y=100)
clock = tk.Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

# labels
label1 = tk.Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#00aeef")
label1.place(x=235, y=600)

label2 = tk.Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#00aeef")
label2.place(x=370, y=600)

label3 = tk.Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#00aeef")
label3.place(x=550, y=600)

label4 = tk.Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#00aeef")
label4.place(x=770, y=600)

t = tk.Label(root, font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)

c = tk.Label(root, font=("arial", 15, "bold"), fg="#ee666d")
c.place(x=400, y=250)

w = tk.Label(root, text="...", font=("arial", 15, "bold"), fg="#ee666d")
w.place(x=235, y=640) 

h = tk.Label(root, text="...", font=("arial", 15, "bold"), fg="#ee666d")
h.place(x=395, y=640) 

d = tk.Label(root, text="...", font=("arial", 15, "bold"), fg="#ee666d")
d.place(x=550, y=640) 

p = tk.Label(root, text="...", font=("arial", 15, "bold"), fg="#ee666d")
p.place(x=770, y=640) 

root.mainloop()
