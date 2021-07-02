import requests
import json
import datetime

longitude_latitude="35.42252723830785,139.64312939950295"#Seiko Gakuin

url="https://api.foursquare.com/v2/venues/search"

with open("./access_token.txt") as f:
    access_token = f.read().rstrip()

params={
    "oauth_token":access_token,
    "ll":longitude_latitude,
    "v":datetime.date.today().strftime("%Y%m%d")
}

response =requests.get(url,params=params)

print(response.url)

a=json.loads(response.text)

print(json.dumps(a, indent=4))