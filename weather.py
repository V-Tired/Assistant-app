import requests
import os

api_key = os.environ['API_KEY']
HEADERS = {'X-Api-Key': api_key}


class Weather:
    def __int__(self):
        pass

    def check_weather(self, request):
        input_list = (request.split(" "))
        if "in" in input_list:
            num = input_list.index("in")
        else:
            num = input_list.index("for")
        if "?" in request:
            state = input_list[-1].split("?")[0].title()
        else:
            state = input_list[num + 2].title()
        if "," in request:
            city = input_list[-2].split(",")[0].title()
        else:
            city = input_list[num + 1].title()

        lat, lon = self.get_loc(city, state)

        parameters = {
            'lat': lat,
            'lon': lon
        }
        api_url = "https://api.api-ninjas.com/v1/weather"
        response_code = requests.get(url=api_url, params=parameters, headers=HEADERS)
        response_code.raise_for_status()
        humidity = response_code.json()['humidity']
        temp = int(response_code.json()['temp']) * 9/5 + 32
        humidity = f"The temp is {temp} with a humidity of {humidity}% in {city}, {state}."
        return humidity

    def get_loc(self, city, state):
        parameters = {
            'city': city,
            'state': state,
            'country': "US"
        }
        url = "https://api.api-ninjas.com/v1/geocoding"
        response = requests.get(url=url, params=parameters, headers=HEADERS)
        if response.status_code == requests.codes.ok:
            info = response.json()
            for each in info:
                if each['state'] == state:
                    lat = each['latitude']
                    lon = each['longitude']
                    return lat, lon
                else:
                    return None

        else:
            print("Error:", response.status_code, response.text)


weather = Weather()

