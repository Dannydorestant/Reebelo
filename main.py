from createproducts import createProducts
from uploadtracking import uploadTracking
from retrieveorders import retrieveOrders
from config import getconfiguration
import time




# uploadTracking(getconfiguration())
# last_run_inventory = uploadtracking.time_stamp - current_time
# print("fir"current_time)
# print(uploadtracking.time_stamp)
# print(time.ctime(last_run_inventory))
# time.sleep(300)
#
# uploadTracking(getconfiguration())
# last_run_inventory = uploadtracking.time_stamp - current_time
# print(current_time)
# print(uploadtracking.time_stamp)
# print(time.ctime(last_run_inventory))

while True:
    current_time = time.time()
    try:
        uploadTracking(getconfiguration())
        retrieveOrders(getconfiguration())
        createProducts(getconfiguration())

        time.sleep(300)
    except:
        time.sleep(30)


# Timestamp the run functions, delta stamp time and current time. if previous time delta skip function