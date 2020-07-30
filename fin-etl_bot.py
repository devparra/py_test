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

import requests
from pandas_datareader import data


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
def belwolf():
    # application flags
    error_count = 0
    error_flag = False

    url = 'https://finance.yahoo.com/'

    try:
        request = requests.get(url, timeout=5)

        if request:
            print('Connected to Yahoo Finance ...')
            # main loop, wont stop until all data is collected
            stock = input('Enter stock symbol (Enter 0 to Exit): ')
            if stock is '0':
                sys.exit(0)
            # Universal function call iterating stock list
            package_exchange_data(stock, 'yahoo')
            # print time of post execution
            print(time_stamp())

    except (requests.ConnectionError, requests.Timeout):

        error_count += 1

        if error_count > 3:
            error = str('ERROR: FAILED CONNECTION - finance.yahoo.com')
            # set data of error
            date = time_stamp()
            # designate error log
            logfile = 'datalog.txt'
            append = 'a'
            # open log, write entry
            with open(logfile, mode=append) as log:
                log.write('\n' + error + ' ' + date)
                log.close()
            raise Exception('ERROR: CONNECTION COULD NOT BE ESTABLISHED')

        # extract error
        error = str('Warning: Failed connection - Reattempting: finance.yahoo.com')
        # set data of error
        date = time_stamp()
        # designate error log
        logfile = 'datalog.txt'
        append = 'a'
        # open log, write entry
        with open(logfile, mode=append) as log:
            log.write('\n' + error + ' ' + date)
            log.close()

        # reattempt launching application
        print('WARNING: COULD NOT CONNECT TO YAHOO FINANCE\nReconnecting ...')

        # MUST FIX, BROKEN!!!
        belwolf()  # CANT CALL FUNCTION RECURSIVELY W\O BEING ENDLESS
        # Need to create custom exception or create a way to add one to error flag each pass

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
        print('''Oops! Something went really wrong.'''
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
    belwolf()
