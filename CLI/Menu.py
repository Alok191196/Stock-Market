from threading import Thread

from StocksList import StockList


class Menu(Thread):

    def __init__(self, strategy):
        Thread.__init__(self)
        self.daemon = True
        self.strategy = strategy

    def run(self):
        while True:
            command = int(input("Enter Command"))
            if command == 1:
                instrument_token = int(input("instrument_token"))
                stock = StockList().get_stock(instrument_token)
                s_id = int(input("Strategy Id"))
                self.strategy.create_new_strategy(s_id, stock)

            elif command == 2:
                for strategy in self.strategy.get_running_strategy():
                    print(strategy)

            elif command == 3:
                for strategy in self.strategy.get_triggered_strategy():
                    print(strategy)

            elif command == 4:
                for strategy in self.strategy.get_finished_strategy():
                    print(strategy)

            elif command == 5:
                for stock in StockList().get_stocks_list():
                    print(stock)
            else:
                pass
            pass
