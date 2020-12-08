import requests

api_url = "http://api.openweathermap.org/data/2.5/weather"

city = input("City?   ")

params = {
    "q": city,
    "appid": "1a953ced9418459ba97162c1ad901e36",
    "units": "metric"
}

res = requests.get(api_url, params=params)
#print(res.status_code)
#print(res.headers["Content-Type"])
#print(res.json())

data = res.json()
template = "Current temperature in {} is {}"
print(template.format(city, data["main"]["temp"]))


