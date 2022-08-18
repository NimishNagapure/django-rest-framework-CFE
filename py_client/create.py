from email import header
import json
import requests
header ={'Authorization': 'Bearer af9672b2de90b920f0d773e1fe87fb0709ad9e59'}
endpoint = " http://localhost:8000/api/products/"

data = {
    "title": "Nimish",
    "price": "100"
}
get_response = requests.post(
    endpoint,json=data,headers=header
)  # HTTP GET request
print(get_response.json())

