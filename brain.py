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
    response=requests.get(url,
                           params=params,
                           headers=headers,timeout=5)
    
    data=response.json()
    if data==[]:
        return "sorry sir cooordinates of this city is not available , try changing city or check if it is spelled correctly "
    return data[0]["lat"],data[0]["lon"]

def weather_status(lat,lon):
    url="https://api.open-meteo.com/v1/forecast"
    params={
        "latitude":lat,
        "longitude":lon,
        "current_weather":True

    }
    
    response=requests.get(url,params=params,timeout=5)
    
    data=response.json()
    return data

