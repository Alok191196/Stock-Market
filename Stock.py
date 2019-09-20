from Strategies.Strategy import Strategy


class Stock:

    def __init__(self, instrument_token):
        self.instrument_token = instrument_token
        self.stock_price = []
        self.active_strategy = []

    def append(self, data):
        self.stock_price.append(data)
        self.notify_all_strategy()
        pass

    def notify_all_strategy(self):
        for strategy in self.active_strategy:
            strategy.update()

    def link_strategy(self, strategy):
        self.active_strategy.append(strategy)

    def __str__(self):
        return self.instrument_token
