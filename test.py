import requests
from time import sleep

while True:
    response = requests.get("https://api.hmoon-skills.net/v1/rdb?guid=health")
    if response.status_code != 200:
        print(response.content, response.status_code)
    sleep(3)