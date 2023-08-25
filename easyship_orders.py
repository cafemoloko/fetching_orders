import requests


api_key = " "
shipment_id = " "
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer {api_key}'
}

r = requests.post("https://api.easyship.com/v2/shipments/easyship_shipment_id={shipment_id}", headers=headers)

print(r.text)