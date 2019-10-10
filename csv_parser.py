import csv
from stock import StockPrice
from utils import get_date
from collections import defaultdict


def parse_file(file_name):
    """

    :param file_name:
    :return: returns a map which has stock name -> list of stock prices sorted ascending by date
    """
    all_stock_data = defaultdict(list)
    prev_date_data = ""
    with open(file_name) as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        header = True
        for a_row in reader:
            if not header:
                if not a_row[1]:
                    a_row[1] = prev_date_data
                else:
                    prev_date_data = a_row[1]

                stock = get_stock_data(a_row)

                all_stock_data[stock.stockName].append(stock)
            else:
                header = False

    for a_stock in all_stock_data:
        all_stock_data[a_stock].sort(key=lambda a_stock_price: a_stock_price.date)

    return all_stock_data


def get_stock_data(csv_data):

    return StockPrice(
        stock_name=csv_data[0].strip(),
        price= float(csv_data[2].strip()),
        date=get_date(csv_data[1].strip())
    )




