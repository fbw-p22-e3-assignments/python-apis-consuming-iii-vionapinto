
import requests

import pprint

url = "https://fakerapi.it/api/v1/products?_quantity=47&_price_min=50.0"

headers = {
    "content_type":"application/json"
}

response = requests.get(url, headers=headers)

pprint.pprint(response.json())