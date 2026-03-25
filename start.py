import requests

url = "https://web-production-19fcb.up.railway.app/data"

data = {
    "mensaje": "hola",
    "numero": 123
}

r = requests.post(url, json=data)

print(r.text)