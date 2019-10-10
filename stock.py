
class StockPrice:
    """
    stores stock price for a give date
    """
    def __init__(self, stock_name, price, date):
        self.stockName = stock_name
        self.price = price
        self.date = date


class PurchaseResult:
    """
    Stores a result of when a stock must be bought and at what cost and sold
    given a period
    to optimise the profit
    """
    def __init__(self, buy_date, sell_date, buy_price, sell_price, profit):
        self.buyDate = buy_date
        self.sellDate = sell_date
        self.buyPrice = buy_price
        self.sellPrice = sell_price
        self.profit = profit

    def __eq__(self, other):
        return (isinstance(other, PurchaseResult) and
                self.buyDate == other.buyDate and
                self.sellDate == other.sellDate and
                self.buyPrice == other.buyPrice and
                self.sellPrice == other.sellPrice and
                self.profit == other.profit
                )

