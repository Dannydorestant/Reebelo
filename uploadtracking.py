import json
import os
import requests
import glob
import pandas as pd
import numpy
import time



def convert(o):
    if isinstance(o, numpy.int64): return int(o)
    raise TypeError


def uploadTracking(configuration):
    url = f"{configuration.url}/orders/track"
    filemask = configuration.ship_filemask
    outbox_path = f"{configuration.outbox_path}\\"
    ship_path = f"{outbox_path}\\{filemask}"
    archive_path = fr"{outbox_path}archive\\"

    for filename in glob.glob(ship_path):
        with open(filename, 'r') as shipfile:
            current_file = filename
            shipfiledata = pd.read_csv(shipfile, sep='\t')
            for ship_line in shipfiledata.index:
                payload = json.dumps({
                    "orderNumber": shipfiledata['orderNumber'][ship_line],
                    "carrier": shipfiledata['carrier'][ship_line],
                    "trackingNumber": shipfiledata['trackingNumber'][ship_line],
                    "lineItems": [
                        {
                            "id": shipfiledata['line_id'][ship_line],
                            "quantity": shipfiledata['quantity'][ship_line]
                        }
                    ]
                }, default=convert)
                headers = {
                    'content-type': 'application/json',
                    'x-api-key': configuration.api_key
                }

                response = requests.request("PUT", url, headers=headers, data=payload)
                time.sleep(1)

                if response.ok:
                    with open(configuration.logs_path + "\\reebelo_log.txt", "a") as file:
                        file.write(f"{time.ctime(time.time())}SUCCESS'   {response.text}    {shipfiledata['orderNumber']}   {shipfiledata['carrier']}   {shipfiledata['trackingNumber']}    {shipfiledata['line_id']}   {shipfiledata['quantity']}\n")
                else:
                    with open(configuration.logs_path + "\\reebelo_log.txt", "a") as file:
                        file.write(f"{time.ctime(time.time())}ERROR'    {response.text} {shipfiledata['orderNumber']}   {shipfiledata['carrier']}   {shipfiledata['trackingNumber']}    {shipfiledata['line_id']}   {shipfiledata['quantity']}\n")



                print(response)






        base_filename = current_file.split("\\")
        os.rename(current_file, archive_path + base_filename[-1])


    time_stamp = time.time()

    print('tracking completed')
# Testing Purposes
# uploadTracking()
