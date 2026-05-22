from ui import welcome_message , goodbye_message
from  brain import weather_status,get_coordinates
print(welcome_message())
city=str(input())
coord=get_coordinates(city)
lat=coord[0]
lon=coord[1]
weather_report=weather_status(lat,lon)
print(weather_report)