import customtkinter
import requests
from PIL import Image

app = customtkinter.CTk()
app.geometry("600x500")
app.title("Weather Map")

customtkinter.set_appearance_mode("System")

api_key = ""
build = "http://api.openweathermap.org/data/2.5/weather?"

def kelvin_celcius(kelvin):
    celcius = kelvin - 273.15
    return celcius


def onclick():
    hasil = build+"appid="+api_key+"&q="+entry.get()
    response = requests.get(hasil).json()
    temp = response['main']['temp']
    temp_celcius = kelvin_celcius(temp)

    for widget in app.winfo_children():
        if isinstance(widget, customtkinter.CTkLabel):
            widget.destroy()

    if temp_celcius > 32:
        temp_img = customtkinter.CTkImage(light_image=Image.open("img/sunny.png"), size=(100,100))
        Image_label = customtkinter.CTkLabel(app,image=temp_img,text="")
        Image_label.pack(padx="10",pady="10")
    elif temp_celcius > 22:
        temp_img = customtkinter.CTkImage(light_image=Image.open("img/rain.png"), size=(100,100))
        Image_label = customtkinter.CTkLabel(app,image=temp_img,text="")
        Image_label.pack(padx="10",pady="10")
    else:
        temp_img = customtkinter.CTkImage(light_image=Image.open("img/else.png"), size=(100,100))
        Image_label = customtkinter.CTkLabel(app,image=temp_img,text="")
        Image_label.pack(padx="10",pady="10")
    
    label = customtkinter.CTkLabel(app, text=f"{int(temp_celcius)}", fg_color="transparent", font=("Arial",20))
    label.pack(padx="5")



entry = customtkinter.CTkEntry(app, placeholder_text="Masukkan nama kota",)
button = customtkinter.CTkButton(app, text="Tekan", command=onclick)

entry.pack(padx="30", pady="30")
button.pack(padx="30", pady="30")


app.mainloop()