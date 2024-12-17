import requests
import random
import datetime
from time import sleep
# used for afk earning in the free panel of sillydev
headers = {
    "Authorization": "",
    "Content-Type": "application/json",
    "Accept": "Application/vnd.pterodactyl.v1+json"
}

def getBalance():
    r = requests.get("https://panel.sillydev.co.uk/api/client/store", headers=headers)
    try:
        return r.json()["attributes"]["balance"]
    except:
        print(r.json())
        return 0

def earn_coins():
    while True:
        sleep(random.randint(40,80))
        r = requests.post("https://panel.sillydev.co.uk/api/client/store/earn", headers=headers, data={})

        time = datetime.datetime.now().strftime("%H:%M:%S %d/%m")
        if r.status_code == 204:
            print(f"[{time}] {getBalance()}$ | Coins redeemed")
        elif r.status_code == 429:
            print(f"[{time}] Error 429 | Waiting 60s")
            sleep(60)
        elif r.status_code == 419:
            print(f"[{time}] Error 419 | Verify your APIKEY")
earn_coins()