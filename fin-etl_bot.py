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
from pandas_datareader._utils import RemoteDataError


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


def logger(message):
    # set data of error
    date = time_stamp()
    # designate error log
    logfile = 'datalog.txt'
    append = 'a'
    # open log, write entry
    with open(logfile, mode=append) as log:
        log.write('\n' + message + ' - ' + date)
        log.close()


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
    error_flag = False
    # net_error = NetFail()

    url = 'https://finance.yahoo.com/'

    try:
        request = requests.get(url, timeout=5)

        if request:
            print('\nConnected to Yahoo Finance ...')
            # main loop, wont stop until all data is collected
            stock = input('Enter stock symbol (Enter 0 to Exit): ')
            if stock == '0':
                logger('PROGRAM EXIT 0')
                print('Exiting ...')
                sys.exit(0)
            elif stock == '':
                print('You didn\'t enter anything! Try again')
                belwolf()
            elif stock != '0' and stock == type(int):
                print('Inappropriate input...\nTry again...')
                belwolf()
            else:
                # Universal function call iterating stock list
                package_exchange_data(stock, 'yahoo')
                # print time of post execution

    except (requests.ConnectionError, requests.Timeout):
        # Log error
        logger(str(sys.exc_info()[:1]))
        # set error flag to true
        error_flag = True
        # print error message to user
        print('CONNECTION ERROR: finance.yahoo.com\nPlease check internet connection.')

    except RemoteDataError:
        logger(str(sys.exc_info()[:1]))
        print('COLLECTION ERROR: No Data found\nPlease check input and retry.')
        error_flag = True
        belwolf()

    # catches general system exceptions
    # Ignore warning of 'Exception too broad'
    except Exception:
        logger(str(sys.exc_info()[1]))
        # set error flag to true
        error_flag = True
        # print error message
        print('''Oops! Something went really wrong.'''
              '''\nPlease check log for more information '''
              '''and relaunch the program.''')

    # final check of error flag
    if not error_flag:
        logger('Data export successful!')
        print('Data export successful! ' + time_stamp())
        belwolf()
    return


# Run main application
if __name__ == '__main__':
    belwolf()
