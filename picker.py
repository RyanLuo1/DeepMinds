import time
import datetime
import pandas as pd

# Remember to install/click Certificate.command and Shell command located in Python 3.9 file through MacOS-Applications
#
#
ticker = 'FB'
period1 = int(time.mktime(datetime.datetime(2021, 5, 1, 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2021, 5, 30, 23, 59).timetuple()))
interval = '1wk'

query_string = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true"

df = pd.read_csv(query_string)
print(df)