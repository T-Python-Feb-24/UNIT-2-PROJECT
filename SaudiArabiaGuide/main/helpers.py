from geopy.geocoders import OpenCage
from geopy.distance import geodesic
from datetime import timedelta
from .api_keys import currency_api_key
from .api_keys import distance_api_key
from .api_keys import weather_api_key


# distance method :

geolocator = OpenCage(user_agent="SaudiArabiaGuide", api_key=distance_api_key)

def distanceKm(from_city: str, to_city: str):
    global distance
    from_geocode = geolocator.geocode(from_city)
    to_geocode = geolocator.geocode(to_city)
    if (from_geocode is None) or (to_geocode is None):
        print("unable to get locate city")

    from_coordinates = from_geocode.latitude, from_geocode.longitude
    to_coordinates = to_geocode.latitude, to_geocode.longitude

    distance = geodesic(from_coordinates, to_coordinates).kilometers

    return distance



# currency exchange method:

def currencyExchange():
    while True:
        user_input = input("Enter the amount you want to exchange with its currency (e.g., 20 USD), separated by a space.: ")
        input_values = user_input.split()
        if len(input_values) != 2:
            print(colored("Invalid input. Please provide the amount and currency, separated by a space.",'red'))
            continue

        amount, base_curr = input_values
        if not amount.isnumeric():
            print("Enter Valid Number!")
            continue
        if not checkValidCurr(base_curr):
            continue
        
        while True:
            target_curr = input("Enter Tagret Currency : ")
            if not checkValidCurr(target_curr):
                continue
            break

        url = "https://v6.exchangerate-api.com/v6/{0}/pair/{1}/{2}/{3}".format(currency_api_key, base_curr, target_curr, amount)
        if not checkValidResponse(url):
            print(colored("Something went wrong please try again later",'red'))
            continue

        response = checkValidResponse(url)
        jsn_response = response.json()
        result = jsn_response["conversion_result"]
        print(f"{user_input} = {result} {target_curr}")
       
        return

# weather method:

def getWeather():
    while True:
        city_name: str = input("Enter city name :")
        if not checkValidStr(city_name):
            continue

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={weather_api_key}"
        if not checkValidResponse(url):
            print("error getting weather data")
            continue

        if checkValidResponse(url):
            response = checkValidResponse(url)
            weather_data = response.json()
            # temperature here would be retrived in Kalvin
            temp = weather_data['main']['temp']
            desc = weather_data['weather'][0]['description']
            # converting the temperature to Celsius
            temp_c = temp - 273.15
            print(f"Today's weather in {city_name} is {desc} ,Temperature is: {round(temp_c)}C")
        
        return


# cheak methods

import requests
from requests.exceptions import ConnectionError
from termcolor import colored


def checkValidInt(int_number: int, max_number: int):
    try:
        int_number = int(int_number)
    except:
        print(colored("invalid input, please make sure to enter an integer number!",'red'))
        return None

    if int_number <= 0 or int_number > max_number:
        print(colored(f"Invalid Number, Please Enter Any number from 1 to {max_number}",'red'))
        return None
    else:
        return int_number


def checkValidStr(str_value):
    if not str_value.isalpha():
        print(colored("invalid input, plase make sure to enter a string value!",'red'))
        return False
    else:
        return str_value


def checkValidCurr(curr: str):
    if not curr.isalpha():
        print(colored("Please Enter Vlid currency value",'red'))
        return None

    elif len(curr) != 3:
        print(colored("Please Enter Vlid currency value",'red'))
        return None
    else:
        return curr


def checkValidResponse(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response
        return
    except ConnectionError:
        print(colored("check your internet connection",'red'))


