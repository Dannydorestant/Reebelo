import requests
import json
import time
from order_details import order_details
from config import *


def retrieveOrders(configuration):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filecreated = False
    inbox_path = f"{configuration.inbox_path}\\"

    url = f"{configuration.url}/orders/?page=1&pageSize=100&status=unfulfilled&sortBy=orderDate-desc"

    payload = ""
    headers = {
        'content-type': 'application/json',
        'x-api-key': configuration.api_key
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = json.loads(response.text)

    for order in data['orders']:
        neworder = order_details()
        neworder.order_number = order['order_number']
        neworder.po_number = order['id']
        neworder.order_date = order['processed_at']
        neworder.shipment_date = order['lastDayToDispatch']
        neworder.first_name = order['shipping_address']['first_name']
        neworder.last_name = order['shipping_address']['last_name']
        neworder.address1 = order['shipping_address']['address1']
        neworder.address2 = order['shipping_address']['address2']
        neworder.city = order['shipping_address']['city']
        neworder.state = order['shipping_address']['province_code']
        neworder.country = order['shipping_address']['country_code']
        neworder.zip = order['shipping_address']['zip']
        neworder.financial_status = order['financial_status']
        neworder.total_ship_price = order['total_shipping_price_set']['shop_money']['amount']

        if neworder.financial_status == 'paid':
            if not filecreated:
                order_file = open(f'{inbox_path}\\reebelo_orders_{timestr}.txt', 'a', encoding='utf-8')
                for i in vars(neworder).keys():
                    order_file.write(f'{i}\t')

                filecreated = True

        for order_line in order['line_items']:
            neworder.qty = int(order_line['quantity'])
            neworder.total_price = float(order_line['pre_tax_price'])
            neworder.unit_price = neworder.total_price / neworder.qty
            neworder.sku = order_line['sku']
            neworder.line_id = order_line['id']
            neworder.request_ship_service = order_line['fulfillment_service']

            taxes = 0
            for tax_line in order_line['tax_lines']:
                tax = float(tax_line['price'])
                taxes += tax
                taxes = taxes / neworder.qty

            neworder.tax_str = format(taxes, '.2f')

            if neworder.financial_status == 'paid':
                if filecreated:
                    order_file.write("\n")
                    for i in vars(neworder).values():
                        order_file.write(f'{i}\t')
        order_file.close()
    print('order download completed')




# Testing Purposes
# retrieveOrders(getconfiguration())
