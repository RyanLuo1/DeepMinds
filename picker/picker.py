import time
import datetime
import pandas as pd

# Remember to install/click Certificate.command and Shell command located in Python 3.9 file through MacOS-Applications


# Created a function for ticker, and needed to return df while also printing df to ensure functionality
def picker_select(ticker):
    period1 = int(time.mktime(datetime.datetime(2021, 5, 1, 23, 59).timetuple()))
    period2 = int(time.mktime(datetime.datetime(2022, 6, 13, 23, 59).timetuple()))
    interval = '1d'

    query_string = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true"

    df = pd.read_csv(query_string)
    print(df)
    return df

if __name__ == "__main__":
    ticker = input("Type in a Stock Symbol: ")
    picker_select(ticker)
