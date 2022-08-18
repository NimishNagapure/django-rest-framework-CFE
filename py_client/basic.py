import json
import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = " http://localhost:8000/api/"

# get_response = requests.get(endpoint,params={"Product_id":12},json={"query" : "Hello Nimish !!"}) #HTTP GET request
get_response = requests.post(
    endpoint, json={"title":"Gucchi","content": "Hello Nimish !!","price":"122f"}
)  # HTTP GET request

# print(get_response.headers)
print(get_response.text)  # print the response raw text

# HTTP request --> HTML
# REST API --> JSON

# print(get_response.json()) # print the response as a JSON object

# print(get_response.status_code) # print the response status code
