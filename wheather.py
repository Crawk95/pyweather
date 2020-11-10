from pyowm import OWM
owm = OWM('c5ad22536e14d7fd0ccae65098268e6c',)
place = input("Inpute place: ")
mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
w = observation.weather
temp = w.temperature('celsius')["temp_min"]
if temp < 10:
    print("Dude outside is like in Siberia, wear better")
elif temp < 20:
    print("Dude outside is cold weat better")
if temp > 20:
    print("Dude wear Shirt")
print("now in " + place + " is " + w.detailed_status + " and")
print("outside aproximate temperature is " + str(temp) + "°C")