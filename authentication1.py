import requests

with open("./client_id.txt") as f:
    client_id = f.read().rstrip()
with open("./client_secret.txt") as f:
    client_secret = f.read().rstrip()

print("client_id, client_secret = ", client_id, client_secret)

redirect_uri="https://twitter.com/Akimasa_L"

url = f"https://foursquare.com/oauth2/authenticate?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}"

print(url)

response=requests.get(url)

print(response.url)
