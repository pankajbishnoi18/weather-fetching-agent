import requests
def get_coordinates(city):
    url="https://nominatim.openstreetmap.org/search"
    params={
        "city":city,
        "format":"json"
    }
    headers={
        "User-Agent":"weather app "

    }
    try:

        response=requests.get(url,
                           params=params,
                           headers=headers,timeout=5)
        response.raise_for_status()
        data=response.json()
        if data==[]:
           return "sorry sir cooordinates of this city is not available thus i cant access weather update, try changing city or check if it is spelled correctly"
        
        return data[0]["lat"],data[0]["lon"]
    except requests.exceptions.Timeout:
       
        return  ("request timed out(coordinate API)") 
    except requests.exceptions.RequestException as e:
        
        return (f"coordinate API error: {e}")
    
    

def weather_status(lat,lon):
    url="https://api.open-meteo.com/v1/forecast"
    params={
        "latitude":lat,
        "longitude":lon,
        "current_weather":True

    }
    
    try :
        response=requests.get(url,params=params,timeout=5)
        response.raise_for_status()
    
        data=response.json()
        return data
    except requests.exceptions.Timeout:
        return "request timed out(weather API)"
    except requests.exceptions.RequestExcepton as e:
        return f"weather API error: {e}"
def fetch_weather(city):
    coord=get_coordinates(city)
    if not isinstance(coord,tuple):
        return coord

    lat=coord[0]
    lon=coord[1]
    weather_report=weather_status(lat,lon)
    return weather_report["current_weather"]

