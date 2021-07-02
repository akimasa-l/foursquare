import requests
import json
import datetime

url="https://api.foursquare.com/v2/venues/add"

with open("./access_token.txt") as f:
    access_token = f.read().rstrip()

seiko_gakuin_id="4b5ab582f964a520a1d128e3"
lat="35.42266036983957"
lng="139.64266526479548"
primaryCategoryId="4bf58dd8d48988d13d941735"

params={
    "name":"\u5b66\u9662\u9577\u5ba4",#学院長室
    "oauth_token":access_token,
    "ll":f"{lat},{lng}",
    "v":datetime.date.today().strftime("%Y%m%d"),
    "primaryCategoryId":primaryCategoryId,
    "parentId":seiko_gakuin_id
}

response =requests.post(url,params=params)

print(response.url)

a=json.loads(response.text)

print(json.dumps(a, indent=4))