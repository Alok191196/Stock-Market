from StocksList import StockList


class DataUpdater:

    def __init__(self):
        pass

    def set_data(self):
        pass

    def update(self, data):
        for val in data:
            instrument_token = val["instrument_token"]
            price = val["price"]
            stock = StockList().get_stock(instrument_token)
            stock.append(price)
