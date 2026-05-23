from brain import fetch_weather
from memory import old_convo
from memory import save_city,save_commands
import json
key_commands={
    1:"to get weather status of any city",
    2:"to view past searches",
    3:"to clear the history",
    4:"to shut the bot"
}


def alpha(key):
    command_panel=["1","2","3","4"]
    if key not in  command_panel:
        response=f"user entered invalid command -->[{key}], as system doesnot identify [{key}] as a command"
        save_commands(key,response)
       
        return response
    if key =="2":
        response=old_convo()
        save_commands(key,"user demanded history")
        return response
    if key=="3":
        data=[]
        with open("history.json","w")as file:
            json.dump(data,file,indent=2)
        response= "history cleared,no memory when this session began"
        save_commands(key,response)
        return response
        
    if key=="1":
        city=input("enter the city sir: ")
        response="enter the city sir: "
        answer=fetch_weather(city)
        save_commands(key,response)
        save_city(city)
        
        return answer
    

        