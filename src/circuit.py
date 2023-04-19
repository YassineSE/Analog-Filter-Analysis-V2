from core import Filter
import second_order

class Circuit(Filter, second_order.Second_Order):
    def __init__(self):
