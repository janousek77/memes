import requests

def get_joke():
    r = requests.get('https://official-joke-api.appspot.com/random_joke')
    return r.json()['setup'] + " " + r.json()['punchline']
