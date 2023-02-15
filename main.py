from createproducts import createProducts
from uploadtracking import uploadTracking
from retrieveorders import retrieveOrders
from config import getconfiguration
from datetime import *
import time


def get_time_difference(current_time, last_run):
    delta = current_time - last_run
    return delta.total_seconds()


# Run All functions once and create baseline timestamps-----------------------------------------------------------------
timestamp_tracking_upload = uploadTracking(getconfiguration())
timestamp_order_download = retrieveOrders(getconfiguration())
timestamp_inventory_upload = createProducts(getconfiguration())

# Convert User input intervals from Minutes to Seconds------------------------------------------------------------------
tracking_upload_interval = int(getconfiguration().ship_interval) * 60
order_download_interval = int(getconfiguration().order_interval) * 60
inventory_upload_interval = int(getconfiguration().inv_interval) * 60


# Run Functions in a loop, only if greater than interval delta in configuration file------------------------------------
while True:
    current_time = datetime.now()
    try:
        if get_time_difference(current_time, timestamp_tracking_upload) > tracking_upload_interval:
            timestamp_tracking_upload = uploadTracking(getconfiguration())
        else:
            pass

        if get_time_difference(current_time, timestamp_order_download) > order_download_interval:
            timestamp_order_download = retrieveOrders(getconfiguration())
        else:
            pass

        if get_time_difference(current_time, timestamp_inventory_upload) > inventory_upload_interval:
            timestamp_inventory_upload = createProducts(getconfiguration())
        else:
            pass

        time.sleep(5)

    except:
        time.sleep(5)




