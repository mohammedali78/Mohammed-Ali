import requests
#import os
from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

sourcefile=open('weather report.txt','w')
print ("-------------------------------------------------------------",file=sourcefile)
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time),file=sourcefile)
print ("-------------------------------------------------------------",file=sourcefile)

print ("Current temperature is: {:.2f} deg C".format(temp_city),file=sourcefile)
print ("Current weather desc  :",weather_desc,file=sourcefile)
print ("Current Humidity      :",hmdt, '%',file=sourcefile)
print ("Current wind speed    :",wind_spd ,'kmph',file=sourcefile)
sourcefile.close()
