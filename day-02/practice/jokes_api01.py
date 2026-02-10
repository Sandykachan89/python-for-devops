import requests
""" 
As a DevOps engineeer you should know how to navigate through multiple external endpoints 
and you should know how to switch them with python
"""
pj_url = "https://official-joke-api.appspot.com/random_joke"
dad_joke_url = "https://icanhazdadjoke.com/"

def get_joke(url_type, mood):
    headers = {
        "Accept": "application/json"
    }

    joke = requests.get(url=url_type, headers=headers)
    if mood == "dad":
        final_joke = joke.json()["joke"]
    if mood == "pj":
        final_joke = joke.json() ["setup"] + joke.json() ["punchline"]
    return final_joke

mood = input("Which joke would you like to hear? eg. (Dad, PJ)") 
if mood == "dad":
    url_type = dad_joke_url
if mood == "pj":
    url_type = pj_url 
else:
    url_type = dad_joke_url

final_joke = get_joke(url_type, mood)

print(final_joke)
