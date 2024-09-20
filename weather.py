import requests
import os

api_key = os.environ['API_KEY']
HEADERS = {'X-Api-Key': api_key}
LAT = "39.744431"
LONG = "-75.545097"


class Weather:
    def __int__(self):
        pass

    def check_weather(self, request):
        input_list = (request.split(" "))
        num = input_list.index("in")
        if "?" in request:
            state = input_list[-1].split("?")[0].title()
        else:
            state = input_list[num + 2].title()
        if "," in request:
            city = input_list[-2].split(",")[0].title()
        else:
            city = input_list[num + 1].title()

        parameters = {
            'lat': LAT,
            'lon': LONG
        }
        api_url = "https://api.api-ninjas.com/v1/weather"
        response_code = requests.get(url=api_url, params=parameters, headers=HEADERS)
        response_code.raise_for_status()
        humidity = response_code.json()['humidity']
        temp = int(response_code.json()['temp']) * 9/5 + 32
        humidity = f"The temp is {temp} with a humidity of {humidity}% in {city} {state}."
        return humidity
