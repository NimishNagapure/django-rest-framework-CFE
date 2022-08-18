import json
import requests

endpoint = " http://localhost:8000/api/products/17/"

# get_response = requests.get(endpoint,params={"Product_id":12},json={"query" : "Hello Nimish !!"}) #HTTP GET request
get_response = requests.get(
    endpoint
)  # HTTP GET request
print(get_response.json())

