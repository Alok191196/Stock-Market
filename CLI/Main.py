from DataUpdater import DataUpdater
from CLI.Menu import Menu
from DummyStocksData import DummyStockData
from Strategies.Strategy import Strategy

if __name__ == '__main__':
    strategy = Strategy()
    m = Menu(strategy)
    m.start()

    data_updater = DataUpdater()
    dummy = DummyStockData(data_updater)
    dummy.start()

    dummy.join()
    m.join()
