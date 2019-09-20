import time
from Strategies.DemoStrategy import DemoStrategy


class Strategy:

    def __init__(self):
        self.running_strategy = []
        self.triggered_strategy = []
        self.finished_strategy = []
        pass
        # self.Stock = stock

    def get_running_strategy(self):
        return self.running_strategy

    def get_triggered_strategy(self):
        return self.running_strategy

    def get_finished_strategy(self):
        return self.finished_strategy

    def update_triggered_strategy(self, strategy):
        self.triggered_strategy.append(strategy)

    def update_finished_strategy(self, strategy):
        self.finished_strategy.append(strategy)

    def create_new_strategy(self, s_id, stock):
        if s_id == 1:
            demo_strategy = DemoStrategy(stock, self)
            self.running_strategy.append(demo_strategy)
        pass
