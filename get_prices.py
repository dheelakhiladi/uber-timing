import uber_rides as uber
import json
import pandas as pd
from uber_rides.session import Session
from uber_rides.client import UberRidesClient
import datetime as dt
import time as t
session = Session(server_token='Bt1pcX8el9rGTOHOciSHnjKmf6wG6BbsfY3Inu-F')
client = UberRidesClient(session)
response = client.get_price_estimates(
            #product_id='c58b6622-0be7-4de1-ad60-a9c4d6f4eaa5',
            start_latitude=13.0878,
            start_longitude=80.1735,
            end_latitude=13.0389,
            end_longitude=80.1474,
        )

now = dt.datetime.now()
hour = str(now.hour)
minute = str(now.minute)
day = str(now.day)
fare_time = hour + ":" + minute


fare = response.json.get('prices')
product_name = fare[9]['display_name']
avg_fare = (fare[9]['high_estimate'] + fare[9]['low_estimate'])/2
data = {'product':[product_name],'price':[avg_fare],'time':[fare_time]}
fare = pd.DataFrame(data = data)

csvrow = fare.to_csv()

file = "uber_fare_data_office_to_home_"+day+"_"+hour+"_"+minute+".csv"
with open(file,'w') as fd:
	fd.write(csvrow)
	fd.close()
while 1:
	t.sleep(240)
	response = client.get_price_estimates(
           	#product_id='c58b6622-0be7-4de1-ad60-a9c4d6f4eaa5',
            start_latitude=13.0878,
            start_longitude=80.1735,
            end_latitude=13.0389,
            end_longitude=80.1474,
        )

	now = dt.datetime.now()
	hour = str(now.hour)
	minute = str(now.minute)
	fare_time = hour + ":" + minute
	print (fare_time)

	fare = response.json.get('prices')
	product_name = fare[9]['display_name']
	avg_fare = (fare[9]['high_estimate'] + fare[9]['low_estimate'])/2
	data = {'product':[product_name],'price':[avg_fare],'time':[fare_time]}
	fare = pd.DataFrame(data = data)
	

	csvrow = fare.to_csv(header=False)
	with open(file,'a') as fd:
		fd.write(csvrow)
	
	pass