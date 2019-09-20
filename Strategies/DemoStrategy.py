import time


class DemoStrategy():

    def __init__(self, stock, strategy):
        self.stock = stock
        self.strategy = strategy
        self.triggered = False
        self.stock.link_strategy(self)
        pass

    def analysis(self):
        print("processing ... ")
        time.sleep(5)
        print("Got Buy Trigger ... ")
        if not self.triggered:
            self.trigger()
        else:
            self.exit()

    def trigger(self):
        self.triggered = True
        self.strategy.update_triggered_strategy(self)
        pass
        # self.manager.insert(self)

    def update(self):
        self.analysis()
        pass

    def exit(self):
        self.strategy.update_finished_strategy(self)
        pass

    def __str__(self):
        return "Demo Strategy"
