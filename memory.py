import json
from brain import fetch_weather
from ui import welcome_message,goodbye_message
def old_convo():
    with open("history.json","r")as file:
        data=json.load(file)
        return data
def save_commands(key,response):
    old_data=old_convo()
    with open("history.json","w") as file:
        command_data={
                "user commanded":key,
                "bot responded":response
            }
        
        old_data.append(command_data)
        json.dump(old_data,file,indent=4)
def save_city(city):
    old_data=old_convo()
    with open("history.json","w") as file:
        command_data={
                "user asked update on ":city,
                "bot responded":fetch_weather(city)
            }
        
        old_data.append(command_data)
        json.dump(old_data,file,indent=4)
def start_session():
    old_data=old_convo()
    with open("history.json","w")as file:
        new={
            "NEW SESSION":f"{welcome_message()}____________________________________________________________________________"}
        old_data.append(new)
        json.dump(old_data,file,indent=4)

def end_session():
    old_data=old_convo()
    with open("history.json","w")as file:
        new={
            "END OF THIS SESSION":f"{goodbye_message()}_____________________________________________________________________"}
        old_data.append(new)
        json.dump(old_data,file,indent=4)

      