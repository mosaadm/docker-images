import requests
import random

url = "http://host.docker.internal:8080"
names = ["name1", "name2", "name3", "name4", "name5"]

name = random.choice(names)
r = requests.post(url, data = name)
print("Status: {} and text: {}".format(r.status_code, name))
