import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from config import *
import json
import requests

#  ADD A Test Connection function to GUI


def update_config():
    current_config = configuration()
    current_config.url = input_URL.get()
    current_config.api_key = input_api_key.get()
    current_config.inbox_path = input_Inbox_path.get()
    current_config.outbox_path = input_Outbox_path.get()
    current_config.order_interval = input_order_download_interval.get()
    current_config.ship_interval = input_shipping_upload_interval.get()
    current_config.inv_interval = input_inventory_upload_interval.get()
    current_config.ship_filemask = input_shipping_upload_filemask.get()
    current_config.inv_filemask = input_inventory_upload_filemask.get()

    print(vars(current_config))

    with open("account_config.txt", "w") as file:
        file.write(json.dumps(vars(current_config)))


def onClick():
    getconfiguration()

    url = f"{getconfiguration().url}/orders/?page=1&pageSize=100&status=unfulfilled&sortBy=orderDate-desc"

    payload = ""
    headers = {
        'content-type': 'application/json',
        'x-api-key': getconfiguration().api_key
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.ok:
        tkinter.messagebox.showinfo("Connection Test", "Connection Successful")
        print('success')
    else:
        tkinter.messagebox.showinfo("Connection Test", f"Connection Failed:{response.text}")




getconfiguration()
print(vars(getconfiguration()))
# Create GUI window
window = Tk()
window.title("Reebelo API Configuration")

# Simply set the theme
window.tk.call("source", "azure.tcl")
window.tk.call("set_theme", "light")

tabs = ttk.Notebook(window)
api_config_tab = Frame(tabs)
upload_download_tab = Frame(tabs)
logs_tab = Frame(tabs)

tabs.add(api_config_tab, text='API Setup')
tabs.add(upload_download_tab, text='Upload/Download Setup')
tabs.add(logs_tab, text='Logs')
tabs.grid(row=0, column=0)




# Api Credentials Config: ----------------------------------------------------------------------------------------------
# Canvas - Api Credentials Config
api_config_canvas = Canvas(api_config_tab)
api_config_canvas.grid(row=0, column=0, padx=10, pady=10)

# Labels - Api Credentials Config

api_endpoint = Label(api_config_canvas, text="API URL: ")
api_endpoint.grid(row=1, column=0, padx=5, pady=5)

current_api_key = Label(api_config_canvas, text="API key: ")
current_api_key.grid(row=2, column=0, padx=5, pady=5)


# User Input - Api Credentials Config
input_URL = ttk.Entry(api_config_canvas, width=40)
if getconfiguration().url is not None:
    input_URL.insert(END, getconfiguration().url)
input_URL.grid(row=1, column=1, padx=5, pady=5)

input_api_key = ttk.Entry(api_config_canvas, width=40)
if getconfiguration().api_key is not None:
    input_api_key.insert(END, getconfiguration().api_key)
input_api_key.grid(row=2, column=1, padx=5, pady=5)

# Test Connection Button
test_api_button = ttk.Button(api_config_canvas, text="Test Connection", command=onClick)
test_api_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)


# File Path Configuration ----------------------------------------------------------------------------------------------
# Canvas - Interval Configuration
file_path_canvas = Canvas(upload_download_tab)
file_path_canvas.grid(row=1, column=0, padx=10, pady=10)


# Labels - File Path Configuration
Inbox_path = Label(file_path_canvas, text="Inbox File Path: ")
Inbox_path.grid(row=1, column=0, padx=5, pady=5)

Outbox_path = Label(file_path_canvas, text="Outbox File Path: ")
Outbox_path.grid(row=2, column=0, padx=5, pady=5)


# Input - File Path Configuration
input_Inbox_path = ttk.Entry(file_path_canvas, width=40)
if getconfiguration().inbox_path is not None:
    input_Inbox_path.insert(END, getconfiguration().inbox_path)
input_Inbox_path.grid(row=1, column=1, padx=5, pady=5)

input_Outbox_path = ttk.Entry(file_path_canvas, width=40)
if getconfiguration().outbox_path is not None:
    input_Outbox_path.insert(END, getconfiguration().outbox_path)
input_Outbox_path.grid(row=2, column=1, padx=5, pady=5)


# Intervals Configuration ----------------------------------------------------------------------------------------------
# Canvas - Interval Configuration
interval_canvas = Canvas(upload_download_tab)
interval_canvas.grid(row=2, column=0, padx=10, pady=10)

# Labels - Interval Configuration
order_download_interval = Label(interval_canvas, text="Order Download Interval (mins): ")
order_download_interval.grid(row=0, column=0, padx=5, pady=5)

shipping_upload_interval = Label(interval_canvas, text="Shipping Upload Interval (mins): ")
shipping_upload_interval.grid(row=2, column=0, padx=5, pady=5)

inventory_upload_interval = Label(interval_canvas, text="Inventory Upload Interval (mins): ")
inventory_upload_interval.grid(row=4, column=0, padx=5, pady=5)

# Entry - Interval Configuration
input_order_download_interval = ttk.Entry(interval_canvas, width=5)
if getconfiguration().order_interval is not None:
    input_order_download_interval.insert(END, getconfiguration().order_interval)
input_order_download_interval.grid(row=0, column=1, padx=5, pady=5)

input_shipping_upload_interval = ttk.Entry(interval_canvas, width=5)
if getconfiguration().ship_interval is not None:
    input_shipping_upload_interval.insert(END, getconfiguration().ship_interval)
input_shipping_upload_interval.grid(row=2, column=1, padx=5, pady=5)

input_inventory_upload_interval = ttk.Entry(interval_canvas, width=5)
if getconfiguration().inv_interval is not None:
    input_inventory_upload_interval.insert(END, getconfiguration().inv_interval)
input_inventory_upload_interval.grid(row=4, column=1, padx=5, pady=5)

# Labels - Filemask Configuration
shipping_upload_filemask = Label(interval_canvas, text="Shipping Upload Filemask: ")
shipping_upload_filemask.grid(row=1, column=0, padx=5, pady=5)

inventory_upload_filemask = Label(interval_canvas, text="Inventory Upload Filemask: ")
inventory_upload_filemask.grid(row=3, column=0, padx=5, pady=5)

# Entry - Filemask Configuration
input_shipping_upload_filemask = ttk.Entry(interval_canvas, width=15)
if getconfiguration().ship_filemask is not None:
    input_shipping_upload_filemask.insert(END, getconfiguration().ship_filemask)
input_shipping_upload_filemask.grid(row=1, column=1, padx=5, pady=5)

input_inventory_upload_filemask = ttk.Entry(interval_canvas, width=15)
if getconfiguration().inv_filemask is not None:
    input_inventory_upload_filemask.insert(END, getconfiguration().inv_filemask)
input_inventory_upload_filemask.grid(row=3, column=1, padx=5, pady=5)

# Functions Configuration ----------------------------------------------------------------------------------------------
# Canvas - Functions Configuration
functions_canvas = Canvas(window)
functions_canvas.grid(row=1, column=0)

start_api_button = ttk.Button(functions_canvas, text="Start Service")
start_api_button.grid(row=0, column=0, padx=5, pady=5)

stop_api_button = ttk.Button(functions_canvas, text="Stop Service")
stop_api_button.grid(row=0, column=1, padx=5, pady=5)

save_config = ttk.Button(functions_canvas, text="Save Config", command=update_config)
save_config.grid(row=0, column=2, padx=5, pady=5)






window.mainloop()
