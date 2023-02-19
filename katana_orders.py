import requests

url = "https://api.katanamrp.com/v1/sales_orders?limit=5"

api_key = " "

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key}"
}

response = requests.get(url, headers=headers)

print(response.text)