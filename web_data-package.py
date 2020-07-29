# Application will collect and package stock exchange data into CSV files
# This data is historical and does not reflect beyond daily changes
#
# Future use of application:
# This application could be extended by adding the option to use any listing
# Further more the application could be extended to use any exchange
# This application could then be altered to detect previously created files and append those files
#
import datetime
import sys

from pandas_datareader import data

# Universal data, stock list and exchange
STOCK_LIST = [
    'INTC',
    'XLNX',
    'PYPL',
    'FB',
    'GOOG',
    'GOOGL',
    'TWTR',
    'AMZN',
    'MSFT',
    'NFLX',
    'IBM',
    'BIDU',
    'ORCL',
    'NVDA',
    'SPOT',
    'PANDY',
    'MU',
]

EXCHANGE = 'yahoo'


# procedural function for creating a timestamp
def time_stamp():
    # create current date and time variables
    current_date = datetime.date.today()
    current_time = datetime.datetime.now()
    # set current date and time
    date = current_date.strftime('%A %B %d, %Y')
    c_time = current_time.strftime('%I:%M %p')
    # concat the date and time
    # Format: WEEKDAY> <MONTH> <DATE>, <YEAR> <HOURS>:<MINUTES> <AM\PM>
    present_dt = str(date + ' ' + c_time)
    return present_dt


# procedural data package function of data
def package_exchange_data(stock, ex):
    # set start and end dates for data reader
    start = datetime.datetime(2015, 1, 1)
    end = datetime.date.today()
    # set stock and dates to data reader
    ticker = data.DataReader(stock, ex, start, end)
    # set file name to stock
    file = str(stock + '.csv')
    # return stock as csv file
    return ticker.to_csv(file, index=True)


# Main function for stock data
def stock_data():
    try:

        # application flags
        error_flag = False
        start_flag = True

        # main loop, wont stop until all data is collected
        while start_flag:
            # loops through stock list
            for stock in range(len(STOCK_LIST)):
                # Universal function call iterating stock list
                package_exchange_data(STOCK_LIST[stock], EXCHANGE)
                # print time of post execution
                print(time_stamp())
            # once loop is done, set start flag to start
            start_flag = False

    # catch exceptions
    except Exception:
        # extract error
        error = str(sys.exc_info()[1])
        # set data of error
        date = time_stamp()
        # designate error log
        logfile = 'datalog.txt'
        append = 'a'
        # open log, write entry
        with open(logfile, mode=append) as log:
            log.write('\n' + error + ' ' + date)
            log.close()
        # set error flag to true
        error_flag = True
        # print error message
        print('''Oops! Something went wong.'''
              '''\nPlease check log for more information '''
              '''and relaunch the program.''')

    # final check of error flag
    if not error_flag:
        # designate error log
        logfile = 'datalog.txt'
        append = 'a'
        # set success log entry
        notice = 'Data export successful!'
        # set date
        date = time_stamp()
        # open log, set entry
        with open(logfile, mode=append) as log:
            log.write('\n' + notice + ' ' + date)
            log.close()

    return


# Run main application
if __name__ == '__main__':
    stock_data()
