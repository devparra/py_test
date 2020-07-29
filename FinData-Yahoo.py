from pandas_datareader import data
import pandas as pd

import datetime
import dtstamp
import sys


def main():

    try:
        errorFlag = False
        date = dtstamp.timeStamp()

        start = datetime.datetime(2015, 1, 1)
        end = datetime.datetime(2019, 8, 26)

        # INTC = data.DataReader('INTC', 'yahoo', start, end)
        # XLNX = data.DataReader('XLNX', 'yahoo', start, end)
        # PYPL = data.DataReader('PYPL', 'yahoo', start, end)
        FB = data.DataReader('FB', 'yahoo', start, end)
        # GOOG = data.DataReader('GOOG', 'yahoo', start, end)
        GOOGL = data.DataReader('GOOGL', 'yahoo', start, end)
        # TWTR = data.DataReader('TWTR', 'yahoo', start, end)
        AMZN = data.DataReader('AMZN', 'yahoo', start, end)
        # MSFT = data.DataReader('MSFT', 'yahoo', start, end)
        NFLX = data.DataReader('NFLX', 'yahoo', start, end)
        # IBM = data.DataReader('IBM', 'yahoo', start, end)
        # BIDU = data.DataReader('BIDU', 'yahoo', start, end)
        # ORCL = data.DataReader('ORCL', 'yahoo', start, end)
        # NVDA = data.DataReader('NVDA', 'yahoo', start, end)
        # SPOT = data.DataReader('SPOT', 'yahoo', start, end)
        # PANDY = data.DataReader('PANDY', 'yahoo', start, end)
        # MU = data.DataReader('MU', 'yahoo', start, end)

        # tickers = ['INTC', 'XLNX', 'PYPL', 'FB', 'GOOG', 'GOOGL', 'TWTR', 'AMZN', 'MSFT', 'NFLX',
        #            'IBM', 'BIDU', 'ORCL', 'NVDA', 'SPOT', 'PANDY', 'MU']

        # tech_stocks = pd.concat([INTC, XLNX, PYPL, FB, GOOG, GOOGL, TWTR, AMZN,
        #                          MSFT, NFLX, IBM, BIDU, ORCL, NVDA, SPOT, PANDY,
        #                          MU], axis=1, keys=tickers)

        # tech_stocks.columns.names = ['Bank Ticker', 'Stock Info']

        # tech_data = pd.DataFrame(tech_stocks)

        # To keep column names and dates, set index to true
        # tech_data.to_csv('Tech_data.csv', index=True,)
        FB.to_csv('facebook.csv', index=True)
        AMZN.to_csv('amazon.csv', index=True)
        NFLX.to_csv('netflix.csv', index=True)
        GOOGL.to_csv('google.csv', index=True)

    except Exception:
        error = str(sys.exc_info()[1])
        logFile = 'datalog.txt'
        append = 'a'
        with open(logFile, mode=append) as logEntery:
            logEntery.write('\n' + error + ' ' + date)
            logEntery.close()
        errorFlag = True
        print('''Oops! Something went worng.'''
              '''\nPlease check log for more information '''
              '''and relaunch the program.''')
    if not errorFlag:
        logFile = 'datalog.txt'
        append = 'a'
        notice = 'Data export succesful!'
        with open(logFile, mode=append) as logEntery:
            logEntery.write('\n' + notice + ' ' + date)
            logEntery.close()
    return

main()

