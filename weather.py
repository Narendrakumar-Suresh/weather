import requests

from datetime import datetime

api_key="a66c3d2d543c78290d9f94f01114ce02"
location=input("Enter city name:")

api_link_='https://api.openweathermap.org//data//2.5//weather?q='+location+'&appid='+api_key
api_link=requests.get(api_link_)
api_data=api_link.json()


temp_city = ((api_data['main']['temp']) - 273.15)
weather_descrip=api_data['weather'][0]['description']
humidity=api_data['main']['humidity']
wind_speed=api_data['wind']['speed']
date_time_=datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("---------------------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time_))
print("---------------------------------------------------------------------------")

print("Current temperature is{:.2f} deg C".format(temp_city))
print("Current weather description:",weather_descrip)
print ("Current Humidity      :",humidity, '%')
print ("Current wind speed    :",wind_speed ,'kmph')

Nk =open ('NKJK.txt',"w")
Nk.write("---------------------------------------------------------------------------"+"\n")
Nk.write("Weather Stats for - {}  || {}".format(location.upper(), date_time_) + "\n")
Nk.write("---------------------------------------------------------------------------" + "\n")
Nk.write("Current temperature is{:.2f} deg C".format(temp_city) + "\n")
Nk.write("Current weather description: "+ weather_descrip + "\n")
Nk.write("Current Humidity      : "+ str(humidity) + '%' + "\n")
Nk.write("Current wind speed    : "+ str(wind_speed) +'kmph' + "\n")
Nk.close()
