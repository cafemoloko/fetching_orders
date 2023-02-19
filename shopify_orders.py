import requests
import json


num_orders = "10"
api_key = " "

url = f"https://{api_key}@luxonis.myshopify.com/admin/api/2021-10/orders.json?limit={num_orders}&fulfillment_status=any"

response = requests.get(url).json()

# created_at (order date)
# note_attributes -> order_number
# line_items -> quantity, sku, title, variant_title
# shipping_address -> country

def filter_data(o):
    obj = {
        "created_at": o["created_at"],
        "order_number": o["order_number"],
        "fulfillment_status": o["fulfillment_status"],
        "order_country": o["shipping_address"]["country"],
        "items": list(map(
            lambda i: {
                "quantity": i["quantity"],
                "sku": i["sku"],
                "title": i["title"],
                "fulfillment_status": i["fulfillment_status"],
                "variant_title": i["variant_title"],
            }
            , o["line_items"]))


    }
    return obj

filtered_data = list(map(filter_data, response["orders"]))

json_data = json.dumps(filtered_data)
print(json_data)
       