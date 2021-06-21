import requests

with open("./code.txt") as f:
    code = f.read().rstrip()

with open("./client_id.txt") as f:
    client_id = f.read().rstrip()
with open("./client_secret.txt") as f:
    client_secret = f.read().rstrip()

print("client_id, client_secret = ", client_id, client_secret)

redirect_uri = "https://twitter.com/Akimasa_L"

print("code is", code)

url = f"https://foursquare.com/oauth2/access_token?client_id={client_id}&client_secret={client_secret}&grant_type=authorization_code&redirect_uri={redirect_uri}&code={code}"

response =requests.get(url)

print("response.text is",response.text)
