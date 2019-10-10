from csv_parser import parse_file
from utils import *
from interaction_utils import get_stock_name, get_period, output_result
import sys


print("Welcome Agent!")
print("Please wait parsing csv ... ")
print("Enter exit at any point to close the program!")

data = parse_file(sys.argv[1])

while True:

    stock_name = get_stock_name(data)

    from_date, to_date = get_period()
    stock_prices = get_stock_prices_in_period(
        all_stock_data=data,
        stock_name=stock_name,
        from_date=from_date,
        to_date=to_date
    )
    mean = get_stock_mean_value_in_period(stock_prices)
    deviation = get_stock_standard_deviation_in_period(stock_prices)
    purchase_result = get_stock_purchase_sell_dates(stock_prices)

    output_result(stock_name, mean, deviation, purchase_result)







