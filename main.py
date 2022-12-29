import requests
import json


def createProducts(name,sku,price,stock):
  url = "https://a.reebelo.com/sockets/offers/update"

  payload = json.dumps({
    "data": [
      {
        "name": "IP11-BLACK-128-GradeB",
        "sku": "testingsku",
        "price": 100,
        "stock": 99
      }
    ]
  })
  headers = {
    'content-type': 'application/json',
    'x-api-key': 'u8DdRNzQJhJMWx3uc97baHbTH'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)



def retrieveOrders:
  url = "https://a.reebelo.com/sockets/orders?page=1&pageSize=20&status=unfilfilled&sortBy=orderDate-desc"

  payload = ""
  headers = {
    'content-type': 'application/json',
    'x-api-key': 'u8DdRNzQJhJMWx3uc97baHbTH'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  print(response.text)

def uploadTracking
  import requests
  import json

  url = "https://a.reebelo.com/sockets/orders/track"

  payload = json.dumps({
    "orderNumber": 1234,
    "carrier": "Australia Post",
    "trackingNumber": "abcdef123456",
    "lineItems": [
      {
        "id": 4568923,
        "quantity": 1
      }
    ]
  })
  headers = {
    'content-type': 'application/json',
    'x-api-key': 'u8DdRNzQJhJMWx3uc97baHbTH'
  }

  response = requests.request("PUT", url, headers=headers, data=payload)

  print(response.text)
