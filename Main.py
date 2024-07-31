import requests

data = requests.get("https://www.realmadrid.com/en-US")

with open("index.html","wb") as f:
    f.write(data.content)