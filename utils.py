from __future__ import division
from datetime import datetime
from math import sqrt
from difflib import get_close_matches
from stock import PurchaseResult


def get_date(date_string):
    return datetime.strptime(date_string, "%d-%m-%Y").date()


def get_mean(sequence):
    return sum(sequence) / len(sequence)


def get_stock_prices_in_period(all_stock_data, stock_name, from_date, to_date):
    return filter(lambda a_stock_price: from_date <= a_stock_price.date <= to_date, all_stock_data[stock_name])


def get_stock_mean_value_in_period(stock_prices):
    return get_mean(map(lambda a_stock_price: a_stock_price.price, stock_prices))


def get_stock_standard_deviation_in_period(stock_prices):

    mean = get_stock_mean_value_in_period(stock_prices)
    return sqrt(get_mean(map(lambda a_stock_price: (a_stock_price.price - mean)**2, stock_prices)))


def get_stock_purchase_sell_dates(stock_prices):

    max_profit = stock_prices[1].price - stock_prices[0].price
    min_stock_value = stock_prices[0].price
    buy_date = stock_prices[0].date
    curr_min_stock_date = stock_prices[0].date
    max_stock_date = stock_prices[1].date

    buy_value = min_stock_value
    sell_value = stock_prices[1].price

    for stock_price in stock_prices[1:]:
        if stock_price.price - min_stock_value > max_profit:
            max_profit = stock_price.price - min_stock_value
            max_stock_date = stock_price.date
            buy_date = curr_min_stock_date
            sell_value = stock_price.price
            buy_value = min_stock_value

        if stock_price.price < min_stock_value:
            min_stock_value = stock_price.price
            curr_min_stock_date = stock_price.date

    return PurchaseResult(
        buy_date, max_stock_date, buy_value, sell_value, max_profit
    )


def get_stock_name_suggestion(input_name, all_stock_data):
    return get_close_matches(input_name, all_stock_data.keys())


