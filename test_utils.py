import unittest
from utils import get_stock_mean_value_in_period, get_stock_standard_deviation_in_period,get_stock_purchase_sell_dates
from stock import StockPrice,PurchaseResult
from datetime import date, timedelta


class TestGetStockMeanValueInPeriod(unittest.TestCase):
    def test_default(self):
        self.assertEqual(
            get_stock_mean_value_in_period(stock_prices=get_test_stock_data()),
            5.5,
            "Should be 5.5"
        )


class TestGetStockStandardDeviationInPeriod(unittest.TestCase):

    def test_default(self):
        self.assertAlmostEqual(
            get_stock_standard_deviation_in_period(get_test_stock_data()),
            2.872281323,
            4,
            "Failed standard deviation"
        )


class TestGetStockPurchaseSellDates(unittest.TestCase):

    def test_default(self):
        self.assertTrue(
            PurchaseResult(
                date(2019, 2, 2),
                date(2019, 2, 11),
                1,
                10,
                9
            ) == (get_stock_purchase_sell_dates(get_test_stock_data()))
        )

    def test_custom_stocks_data(self):
        self.assertTrue(
            PurchaseResult(
                date(2019, 2, 4),
                date(2019, 2, 7),
                2,
                18,
                16
            ) == (get_stock_purchase_sell_dates(get_test_stock_data_2()))
        )


def get_test_stock_data():
    start = date(2019, 2, 1)
    data = []
    for i in range(1, 11):
        data.append(StockPrice(
            "tst",
            i,
            start + timedelta(days=i)
        ))

    return data


def get_test_stock_data_2():
    prices = [10,4,2,12,5,18,2,10,15,8]
    start = date(2019, 2, 1)
    data = []
    for i in range(1, 11):
        data.append(StockPrice(
            "tst",
            prices[i-1],
            start + timedelta(days=i)
        ))

    return data


if __name__ == '__main__':
    unittest.main()