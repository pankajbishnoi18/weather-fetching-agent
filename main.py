from ui import welcome_message , goodbye_message
from  brain import weather_status,get_coordinates,fetch_weather
from weather_command import key_commands,alpha
from memory import start_session,end_session
import json
print(welcome_message())
print(key_commands)
start_session()





while True:
    key=input()
    print(alpha(key))
    if key=="4":
        print(goodbye_message())
        end_session()
        break



#there is error as memory and weather_command are importing each other 
#still have to add those start session and end session feature , not even tested once ,there could be lot more to fix
        