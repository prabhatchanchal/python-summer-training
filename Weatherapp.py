from tkinter import *
import requests as rq
import json
global main_window
main_window=Tk()
main_window.title("WEATHER NOW")
main_window.iconbitmap(r'weathernow.ico')
main_window.minsize(300,227)
main_window.configure(background="sandy brown")

#images***********************

rain_icon = PhotoImage(file="Status-weather-showers-icon.png")
# haze_icon=PhotoImage(file="")
haze_icon=PhotoImage(file="Screenshot (12).png")
sun_icon=PhotoImage(file="sunny-icon.png")
clear_icon=PhotoImage(file="Status-weather-clear-icon.png")

#***********default location*********************

ip=rq.get("https://ipinfo.io/")
codepin=json.loads(ip.text)
pincode=codepin["postal"]
responce1 = rq.get(f"https://api.openweathermap.org/data/2.5/weather?zip={pincode},in&appid=dc581f11fa7c40695b28d04a8fe47692")
json_file = json.loads(responce1.text)
blankleft=Label(main_window,bg="sandy brown", width =10)
blankleft.grid(row=0,column=0)
blankright=Label(main_window,bg="sandy brown", width =10)
blankright.grid(row=0,column=2)
labelcity=Label(main_window, bg="sandy brown",font="Bahnschrift",width=25,text="your city is : "+ codepin["city"])
labelcity.grid(row=4,column=1)
defaultText = Label(main_window, text=json_file["weather"][0]["main"]+" "+json_file["weather"][0]["description"],width=25,bg="sandy brown",font="bold")
defaultText.grid(row=5, column=1)
defaultIcon = Label(main_window, image=clear_icon,width=227)
defaultIcon.grid(row=6,column=1)


#***********end of default location**********************
labelpressure=Label(main_window, bg="oliveDrab1",font="bold",width=25,text="pressure : "+str(json_file["main"]["pressure"]))
labelpressure.grid(row=7,column=1)
labeltemp=Label(main_window, bg="oliveDrab1",font="bold",width=25,text="temprature : "+str(json_file["main"]["temp"]))
labeltemp.grid(row=8,column=1)
labeltemp_max=Label(main_window, bg="oliveDrab1",font="bold",width=25,text="max temprature : "+str(json_file["main"]["temp_max"]))
labeltemp_max.grid(row=9,column=1)

labeltemp_min=Label(main_window, bg="oliveDrab1",font="bold",width=25,text="min temprature : "+str(json_file["main"]["temp_min"]))
labeltemp_min.grid(row=10,column=1)
labelhumidity=Label(main_window, bg="oliveDrab1",font="bold",width=25,text="humidity : "+str(json_file["main"]["humidity"]))
labelhumidity.grid(row=11,column=1)
sunrize=str(json_file["sys"]["sunrise"])
labelsunrise=Label(main_window, bg="oliveDrab1",font="bold",width=25,text="sunrise = "+sunrize[:2]+":"+sunrize[2:4]+":"+sunrize[4:6])
labelsunrise.grid(row=12,column=1)
sunset=str(json_file["sys"]["sunset"])
labelsunset=Label(main_window, bg="oliveDrab1",font="bold",width=25,text="sunset = "+sunset[:2]+":"+sunset[2:4]+":"+sunset[4:6])
labelsunset.grid(row=13,column=1)
labelwind=Label(main_window, bg="oliveDrab1",font="bold",width=25,text="windspeed : "+str(json_file["wind"]["speed"]))
labelwind.grid(row=14,column=1)



labelshow=Label(main_window,text="Enter your pin code",font='bold',bd=12,bg='sandy brown')
labelshow.grid(row=0,column=1)
labelentry=Entry(main_window,bg='orange',width=25,font="bold")
labelentry.grid(row=1,column=1)


def onClick():
    pincode=labelentry.get()
    responce = rq.get(f"https://api.openweathermap.org/data/2.5/weather?zip={pincode},in&appid=dc581f11fa7c40695b28d04a8fe47692")
    json_file = json.loads(responce.text)
    if json_file["weather"][0]["main"]=="Clouds":
        labelcity = Label(main_window, bg="sandy brown", font="Bahnschrift", width=25,
                          text="your are at :"+str(json_file["name"]))
        labelcity.grid(row=4, column=1)
        defaultText = Label(main_window, text=json_file["weather"][0]["main"])
        defaultText.grid(row=0, column=0)
        defaultIcon = Label(main_window, image=rain_icon)
        defaultIcon.grid(row=1, column=0)
        labelpressure = Label(main_window, bg="oliveDrab1", font="Bahnschrift", width=25,
                              text="pressure : " + str(json_file["main"]["pressure"]))
        labelpressure.grid(row=7, column=1)
        labeltemp = Label(main_window, bg="oliveDrab1", font="Bahnschrift", width=25,
                          text="temprature : " + str(json_file["main"]["temp"]))
        labeltemp.grid(row=8, column=1)
        labeltemp_max = Label(main_window, bg="oliveDrab1", font="Bahnschrift", width=25,
                              text="max temprature : " + str(json_file["main"]["temp_max"]))
        labeltemp_max.grid(row=9, column=1)
        labeltemp_min = Label(main_window, bg="oliveDrab1", font="Bahnschrift", width=25,
                              text="min temprature : " + str(json_file["main"]["temp_min"]))
        labeltemp_min.grid(row=10, column=1)
        labelhumidity = Label(main_window, bg="oliveDrab1", font="Bahnschrift", width=25,
                              text="humidity : " + str(json_file["main"]["humidity"]))
        labelhumidity.grid(row=11, column=1)
        sunrize = str(json_file["sys"]["sunrise"])
        labelsunrise = Label(main_window, bg="oliveDrab1", font="Bahnschrift", width=25,
                             text="sunrise = " + sunrize[:2] + ":" + sunrize[2:4] + ":" + sunrize[4:6])
        labelsunrise.grid(row=12, column=1)
        sunset = str(json_file["sys"]["sunset"])
        labelsunset = Label(main_window, bg="oliveDrab1", font="Bahnschrift", width=25,
                            text="sunset = " + sunset[:2] + ":" + sunset[2:4] + ":" + sunset[4:6])
        labelsunset.grid(row=13, column=1)
        labelwind = Label(main_window, bg="oliveDrab1", font="Bahnschrift", width=25,
                          text="windspeed : " + str(json_file["wind"]["speed"]))
        labelwind.grid(row=14, column=1)

    elif json_file["weather"][0]["main"]=="Haze":
        labelcity = Label(main_window, bg="sandy brown", font="Bahnschrift", width=25,
                          text="your are at :" + str(json_file["name"]))
        labelcity.grid(row=4, column=1)
        defaultText = Label(main_window, text=json_file["weather"][0]["main"])
        defaultText.grid(row=0, column=0)
        defaultIcon = Label(main_window, image=haze_icon)
        defaultIcon.grid(row=1, column=0)
        labelpressure = Label(main_window, bg="oliveDrab1", font="Bahnschrift", width=25,
                              text="pressure : " + str(json_file["main"]["pressure"]))
        labelpressure.grid(row=7, column=1)
        labeltemp = Label(main_window, bg="oliveDrab1", font="Bahnschrift", width=25,
                          text="temprature : " + str(json_file["main"]["temp"]))
        labeltemp.grid(row=8, column=1)
        labeltemp_max = Label(main_window, bg="oliveDrab1", font="Bahnschrift", width=25,
                              text="max temprature : " + str(json_file["main"]["temp_max"]))
        labeltemp_max.grid(row=9, column=1)
        labeltemp_min = Label(main_window, bg="oliveDrab1", font="Bahnschrift", width=25,
                              text="min temprature : " + str(json_file["main"]["temp_min"]))
        labeltemp_min.grid(row=10, column=1)
        labelhumidity = Label(main_window, bg="oliveDrab1", font="Bahnschrift", width=25,
                              text="humidity : " + str(json_file["main"]["humidity"]))
        labelhumidity.grid(row=11, column=1)
        sunrize = str(json_file["sys"]["sunrise"])
        labelsunrise = Label(main_window, bg="oliveDrab1", font="Bahnschrift", width=25,
                             text="sunrise = " + sunrize[:2] + ":" + sunrize[2:4] + ":" + sunrize[4:6])
        labelsunrise.grid(row=12, column=1)
        sunset = str(json_file["sys"]["sunset"])
        labelsunset = Label(main_window, bg="oliveDrab1", font="Bahnschrift", width=25,
                            text="sunset = " + sunset[:2] + ":" + sunset[2:4] + ":" + sunset[4:6])
        labelsunset.grid(row=13, column=1)
        labelwind = Label(main_window, bg="oliveDrab1", font="Bahnschrift", width=25,
                          text="windspeed : " + str(json_file["wind"]["speed"]))
        labelwind.grid(row=14, column=1)

    elif json_file["weather"][0]["main"]=="Clear":
        labelcity = Label(main_window, bg="sandy brown", font="Bahnschrift", width=25,
                          text="your are at :" + str(json_file["name"]))
        labelcity.grid(row=4, column=1)
        defaultText = Label(main_window, text=json_file["weather"][0]["main"])
        defaultText.grid(row=0, column=0)
        defaultIcon = Label(main_window, image=clear_icon)
        defaultIcon.grid(row=1, column=1)
        labelpressure = Label(main_window, bg="oliveDrab1", font="Bahnschrift", width=25,
                              text="pressure : " + str(json_file["main"]["pressure"]))
        labelpressure.grid(row=7, column=1)
        labeltemp = Label(main_window, bg="oliveDrab1", font="Bahnschrift", width=25,
                          text="temprature : " + str(json_file["main"]["temp"]))
        labeltemp.grid(row=8, column=1)
        labeltemp_max = Label(main_window, bg="oliveDrab1", font="Bahnschrift", width=25,
                              text="max temprature : " + str(json_file["main"]["temp_max"]))
        labeltemp_max.grid(row=9, column=1)
        labeltemp_min = Label(main_window, bg="oliveDrab1", font="Bahnschrift", width=25,
                              text="min temprature : " + str(json_file["main"]["temp_min"]))
        labeltemp_min.grid(row=10, column=1)
        labelhumidity = Label(main_window, bg="oliveDrab1", font="Bahnschrift", width=25,
                              text="humidity : " + str(json_file["main"]["humidity"]))
        labelhumidity.grid(row=11, column=1)
        sunrize = str(json_file["sys"]["sunrise"])
        labelsunrise = Label(main_window, bg="oliveDrab1", font="Bahnschrift", width=25,
                             text="sunrise = " + sunrize[:2] + ":" + sunrize[2:4] + ":" + sunrize[4:6])
        labelsunrise.grid(row=12, column=1)
        sunset = str(json_file["sys"]["sunset"])
        labelsunset = Label(main_window, bg="oliveDrab1", font="Bahnschrift", width=25,
                            text="sunset = " + sunset[:2] + ":" + sunset[2:4] + ":" + sunset[4:6])
        labelsunset.grid(row=13, column=1)
        labelwind = Label(main_window, bg="oliveDrab1", font="Bahnschrift", width=25,
                          text="windspeed : " + str(json_file["wind"]["speed"]))
        labelwind.grid(row=14, column=1)

    # elif json_file["weather"][0]["main"]=="Clear":
    #     defaultText = Label(main_window, text=json_file["weather"][0]["main"]+json_file["weather"][0]["description"])
    #     defaultText.grid(row=0, column=0)
    #     defaultIcon = Label(main_window, image=clear_icon)
    #     defaultIcon.grid(row=1, column=0)
    labelshow.grid_remove()
    labelentry.grid_remove()
    submit_button.grid_remove()
    defaultText.grid_remove()
    defaultIcon.grid_remove()

submit_button=Button(main_window,command=onClick,text="submit",font='pickwick',bd=5,relief='groove')
submit_button.grid(row=3,column=1)
quit_button=Button(main_window,command=lambda :main_window.destroy(),text="QUIT",font='bold',bd=5,relief='groove')
quit_button.grid(row=0,column=3)


quit_button=Button(main_window,command=None,text="show",font='bold',bd=5,relief='groove')
quit_button.grid(row=0,column=0)



main_window.mainloop()
