import requests

url = "http://host.docker.internal:8080"
#payload = {'user': 'name' }
#r =requests.get("http://host.docker.internal:8080", params=payload)
#print(r.url)
r = requests.post(url, data = "name")
print("Status: {} and text: {}".format(r.status_code, r.text))

