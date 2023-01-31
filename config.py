import json

class configuration:
    def __init__(self, inbox_path=None, outbox_path=None, api_key=None, ship_filemask=None, inv_filemask=None,
                 order_interval=None, inv_interval=None, ship_interval=None, logs_path=None, url=None):
        self.inbox_path = inbox_path
        self.outbox_path = outbox_path
        self.api_key = api_key
        self.ship_filemask = ship_filemask
        self.inv_filemask = inv_filemask
        self.order_interval = order_interval
        self.inv_interval = inv_interval
        self.ship_interval = ship_interval
        self.logs_path = logs_path
        self.url = url


def getconfiguration():
    with open('account_config.txt', 'r') as config:
        config_data = json.loads(config.read())
        current_config = configuration()
        current_config.url = config_data['url']
        current_config.api_key = config_data['api_key']
        current_config.inbox_path = config_data['inbox_path']
        current_config.outbox_path = config_data['outbox_path']
        current_config.order_interval = config_data['order_interval']
        current_config.ship_interval = config_data['ship_interval']
        current_config.inv_interval = config_data['inv_interval']
        current_config.ship_filemask = config_data['ship_filemask']
        current_config.inv_filemask = config_data['inv_filemask']
        current_config.logs_path = config_data['logs_path']
        return(current_config)

