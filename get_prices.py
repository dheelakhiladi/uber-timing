import uber_rides as uber
import json
from uber_rides.session import Session
from uber_rides.client import UberRidesClient
session = Session(server_token='Bt1pcX8el9rGTOHOciSHnjKmf6wG6BbsfY3Inu-F')
client = UberRidesClient(session)
response = client.get_products(13.0878,80.1735)
products = response.json.get('products')
print(type(products))