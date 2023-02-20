import requests
import json

api_key = " "
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer {api_key}'
}

r = requests.post("https://api.easyship.com/v2/shipments/easyship_shipment_id=ESHK67789484", headers=headers)

print(r.text)