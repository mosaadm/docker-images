import requests
import random

url = 'http://localhost:8080'
names = ["Michael", "Mos3ad", "Bo2loz", "Fany", "Timy", "Gigi"]

try:
    r = requests.post(url, data=random.choice(names))
    print(r.text)
except:
    print("Could not connect to server %s" % url)
