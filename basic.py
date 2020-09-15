from tkinter import *
import requests
import json

root = Tk()
root.title("Weather App")
root.geometry("700x400")
root.configure(background = "black")

lable_temp = Label(root,text="...",width = 5,bg='white',font=("bold",10),fg='blue')
lable_temp.place(x=192,y=220)

lable_pres = Label(root,text="...",width = 5,bg='white',font=("bold",10),fg='blue')
lable_pres.place(x=192,y=240)




api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Shillong&appid=ce6a3ba3755fe67d075c64bcc797fcbb")
api = json.loads(api_request.content)

y = api['main']
current_temprature = y['temp']
current_pressure = y['pressure']

lable_pres.configure(text=current_pressure)
lable_temp.configure(text=current_temprature)	   
   



myLabel = Label(root, text=api)
myLabel.pack()


root.mainloop()
