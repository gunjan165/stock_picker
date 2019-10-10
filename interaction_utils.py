from utils import get_stock_name_suggestion, get_date
import sys

def get_stock_name(all_stock_data):

    while True:
        print("Which stock do you want to process?")
        input_stock_name = get_user_input()

        if input_stock_name in all_stock_data:
            return input_stock_name
        else:
            suggestions = get_stock_name_suggestion(input_stock_name, all_stock_data)

            for suggestion in suggestions:
                print("Did you mean: " + suggestion, " y or n ")
                choice = get_user_input()

                if choice == "y":
                    return suggestion
            else:
                return get_stock_name(all_stock_data)


def get_period():

    print("From which do you want to start?")
    from_date = get_date_input()
    print("Till which date do you want to analyze")

    to_date = get_date_input()
    while to_date <= from_date:
        print("End date must be greater than start date")
        to_date = get_date_input()
    return from_date,to_date


def get_date_input():
    try:
        return get_date(get_user_input())

    except Exception as e:
        if "range" in e.message:
            print("Please recheck the date!")
        else:
            print("Please enter valid date in format dd-mm-yyyy")
        return get_date_input()


def output_result(stock_name, mean, deviation, purchase_result):

    print("\nHere is the result for : " + stock_name)

    print("Mean value : " + str(mean))

    print("Standard deviation : " + str(deviation))

    print("To maximize profit, "
          "\n\t Buy on : " + purchase_result.buyDate.strftime("%d-%m-%Y") + " at : " + str(purchase_result.buyPrice) +
          "\n\t Sell on: " + purchase_result.sellDate.strftime("%d-%m-%Y")) + " at : " + str(purchase_result.sellPrice)

    print ("Profit assuming 100 shares are bought : " + str(purchase_result.profit * 100) + "\n")

def exit_program():
    print("Exiting ...")
    sys.exit()

def get_user_input():

    user_input = raw_input()

    if user_input.lower() == "exit":
        exit_program()
    else:
        return user_input
    