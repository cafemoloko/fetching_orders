import requests
import json


store_name = " "
api_key = " "
num_orders = " "
status = " "

url = f"https://{api_key}@{store_name}.myshopify.com/admin/api/2021-10/orders.json?limit={num_orders}&fulfillment_status={status}"

response = requests.get(url).json()

# created_at (order date)
# note_attributes -> order_number
# line_items -> quantity, sku, title, variant_title
# shipping_address -> country

def filter_data(order):
    obj = {
        "created_at": order["created_at"],
        "order_number": order["order_number"],
        "fulfillment_status": order["fulfillment_status"],
        "order_country": order["shipping_address"]["country"],
        "items": list(map(
            lambda i: {
                "quantity": i["quantity"],
                "sku": i["sku"],
                "title": i["title"],
                "fulfillment_status": i["fulfillment_status"],
                "variant_title": i["variant_title"],
            }
            , order["line_items"]))

    }
    return obj

filtered_data = list(map(filter_data, response["orders"]))

json_data = json.dumps(filtered_data)
print(json_data)
       