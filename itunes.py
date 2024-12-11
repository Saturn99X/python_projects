import requests
import json
import sys


response = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term=" + "Clovisreyes")

X = response.json()

for result in X["results"]:
    print(result["TrackName"])
 