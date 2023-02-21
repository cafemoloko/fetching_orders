import requests


url = "https://api.katanamrp.com/v1/sales_orders?limit=1"

api_key = " "

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key}"
}

response = requests.get(url, headers=headers).json()


def katana_data(o):
    obj = {
        "id": o["id"],
        "order_number": o["order_no"],
        "location_id": o["location_id"],
    }
    return obj


katana_order = list(map(katana_data, response["data"]))
print(katana_order)