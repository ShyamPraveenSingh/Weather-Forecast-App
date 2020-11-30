#python3 -- Weather Application using API

#importing the libraries
from tkinter import *
import requests
import json
import datetime
from PIL import ImageTk,Image

#necessary details
root = Tk()
root.title("Weather App")
root.geometry("450x700")
root['background'] = "white"


#Image
new = ImageTk.PhotoImage(Image.open('logo.png'))
panel = Label(root,image=new)
panel.place(x=0, y=520)





#Date 

dt = datetime.datetime.now() 
date = Label(root, text = dt.strftime('%A--'), bg='white', font=("bold",15))
date.place(x=5, y=130)
month = Label(root, text = dt.strftime('%m %B'), bg='white', font=("bold",15))
month.place(x=100, y=130)

#Time

hour = Label(root, text = dt.strftime('%I : %M %p'), bg='white', font=("bold",15))
hour.place(x=10, y=160)

if int((dt.strftime('%I'))) >= 8 & int((dt.strftime('%I'))) <=5 :
	img = ImageTk.PhotoImage(Image.open('moon.png'))
	panel = Label(root,image=img)
	panel.place(x=210,y=200)
else:
	img = ImageTk.PhotoImage(Image.open('sun.png'))
	panel = Label(root,image=img)
	panel.place(x=210,y=200)

#City Search
city_name = StringVar()
city_entry = Entry(root, textvariable=city_name, width=45)
city_entry.grid(row=1, column=0, ipady=10, stick=W+E+N+S)




def city_name():
   
	#API Call
	api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city_entry.get() + "&units=metric&appid=ce6a3ba3755fe67d075c64bcc797fcbb")
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
	citi = api['name']
	





	#Adding the info into the screen
	lable_temp.configure(text=current_temprature)
	lable_humidity.configure(text=humidity)
	max_temp.configure(text=tempmax)
	min_temp.configure(text=tempmin)
	lable_lon.configure(text=longtitude)
	lable_lat.configure(text=latitude)
	lable_country.configure(text=country)
	lable_citi.configure(text=citi)

#Search Bar and Button
city_nameButton = Button(root, text="Search", command=city_name)
city_nameButton.grid(row=1, column=1, padx=5, stick=W+E+N+S)




#Country  Names and Coordinates
lable_citi = Label(root, text="...", width = 0, bg='white', font=("bold",15))
lable_citi.place(x=10,y=63)

lable_country = Label(root, text="...", width = 0, bg='white', font=("bold",15))
lable_country.place(x=135,y=63)

lable_lon = Label(root, text="...", width = 0, bg='white', font=("Helvetica",15))
lable_lon.place(x=25,y=95)
lable_lat = Label(root, text="...", width = 0, bg='white', font=("Helvetica",15))
lable_lat.place(x=95,y=95)

#Current Temperature

lable_temp = Label(root,text="...",width = 0,bg='white',font=("Helvetica",110),fg='black')
lable_temp.place(x=18,y=220)

#Temperature Details

humi = Label(root, text="Humidity: ", width = 0, bg='white', font=("bold",15))
humi.place(x=3,y=400)
lable_humidity = Label(root, text="...", width = 0, bg='white', font=("bold",15))
lable_humidity.place(x=107,y=400)

maxi = Label(root, text="Max. Temp.: ", width = 0, bg='white', font=("bold",15))
maxi.place(x=3,y=430)
max_temp = Label(root, text="...", width = 0, bg='white', font=("bold",15))
max_temp.place(x=128,y=430)


mini = Label(root, text="Min. Temp.: ", width = 0, bg='white', font=("bold",15))
mini.place(x=3,y=460)
min_temp = Label(root, text="...", width = 0, bg='white', font=("bold",15))
min_temp.place(x=128,y=460)



note = Label(root, text="All temperatures in degree celsius", bg='white',font=("italic", 10))
note.place(x=95, y=495)



root.mainloop()
