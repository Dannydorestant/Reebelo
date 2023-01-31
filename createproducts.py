import json
import os
import requests
import glob
import pandas as pd
import numpy



def convert(o):
    if isinstance(o, numpy.int64): return int(o)
    raise TypeError


def createProducts(configuration):
    url = f"{configuration.url}/offers/update"
    filemask = configuration.inv_filemask
    outbox_path = f"{configuration.outbox_path}\\"
    inventory_path = f"{outbox_path}\\{filemask}"
    archive_path = fr"{outbox_path}\\archive\\"

    for filename in glob.glob(inventory_path):
        with open(filename, 'r') as invfile:
            current_file = filename
            invfiledata = pd.read_csv(invfile, sep='\t')
            for inv_line in invfiledata.index:
                payload = json.dumps({
                    "data": [
                        {
                            "name": invfiledata['name'][inv_line],
                            "sku": invfiledata['sku'][inv_line],
                            "price": invfiledata['price'][inv_line],
                            "stock": invfiledata['stock'][inv_line]
                        }
                    ]
                }, default=convert)
                headers = {
                    'content-type': 'application/json',
                    'x-api-key': configuration.api_key
                }

                response = requests.request("POST", url, headers=headers, data=payload)
                print(response)

        base_filename = current_file.split("\\")
        os.rename(current_file, archive_path + base_filename[-1])
    print('inv completed')
# Testing Purposes
# createProducts(getconfiguration())
