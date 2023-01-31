
class order_details:
    def __init__(self, order_number=None, po_number=None, order_date=None, shipment_date=None, first_name=None,
                 last_name=None, address1=None, address2=None, city=None, state=None, country=None, zipcode=None,
                 financial_status=None, total_ship_price=None, total_price=None, sku=None, qty=None, unit_price=None,
                 line_id=None, request_ship_service=None, tax_str=None):
        self.order_number = order_number
        self.po_number = po_number
        self.order_date = order_date
        self.shipment_date = shipment_date
        self.first_name = first_name
        self.last_name = last_name
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.country = country
        self.zipcode = zipcode
        self.financial_status = financial_status
        self.total_ship_price = total_ship_price
        self.total_price = total_price
        self.sku = sku
        self.qty = qty
        self.unit_price = unit_price
        self.line_id = line_id
        self.request_ship_service = request_ship_service
        self.tax_str = tax_str

