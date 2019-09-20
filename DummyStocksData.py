from threading import Thread
import time
import random


class DummyStockData(Thread):

    def __init__(self, data_updater):
        Thread.__init__(self)
        self.daemon = True
        self.data_updater = data_updater

    @staticmethod
    def generate_data():
        random.seed(int(time.time()))
        instrument_token = random.choice([101, 102, 103, 104, 105])
        price = random.randrange(100, 200)
        data = [{"instrument_token": instrument_token, "price": price}]
        return data

    def run(self):
        while True:
            data = self.generate_data()
            print(data)
            self.data_updater.update(data)
            time.sleep(5)
