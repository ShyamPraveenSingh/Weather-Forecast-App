from tkinter import *
import requests
import json

root = Tk()
root.title("Weather App")
root.geometry("700x400")
root.configure(background = "white")

#API Call
api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Shillong&units=metric&appid=ce6a3ba3755fe67d075c64bcc797fcbb")
api = json.loads(api_request.content)

#Temperatures
y = api['main']
current_temprature = y['temp']
humidity = y['humidity']
tempmin = y['temp_min']
tempmax = y['temp_max']

#Coordinates
x = api['coord']
longtitude = x['lon']
latitude =  x['lat']

#Country 
z = api['sys']
country = z['country']



#Labels

lable_lon = Label(root,text="...",width = 5,bg='white',font=("bold",10),fg='blue')
lable_lon.place(x=192,y=320)

lable_lat = Label(root,text="...",width = 5,bg='white',font=("bold",10),fg='blue')
lable_lat.place(x=192,y=340)



lable_temp = Label(root,text="...",width = 5,bg='white',font=("bold",10),fg='blue')
lable_temp.place(x=192,y=220)

lable_humid = Label(root,text="...",width = 5,bg='white',font=("bold",10),fg='blue')
lable_humid.place(x=192,y=260)


lable_max = Label(root,text="...",width = 5,bg='white',font=("bold",10),fg='blue')
lable_max.place(x=192,y=300)

lable_min = Label(root,text="...",width = 5,bg='white',font=("bold",10),fg='blue')
lable_min.place(x=192,y=280)


lable_country = Label(root,text="...",width = 5,bg='white',font=("bold",10),fg='blue')
lable_country.place(x=250,y=300)




#Adding the info into the screen
lable_temp.configure(text=current_temprature)
lable_humid.configure(text=humidity)
lable_max.configure(text=tempmax)
lable_min.configure(text=tempmin)
lable_lon.configure(text=longtitude)
lable_lat.configure(text=latitude)
lable_country.configure(text=country)


myLabel = Label(root, text=api)
myLabel.pack()


root.mainloop()
