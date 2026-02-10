import requests

api_url = "https://alexwohlbruck.github.io/cat-facts/"

response = requests.get(url=api_url)

for key,value in response.json().items():
    if key == "userId":
        if value in [1,2,3]:
            print("User Found")