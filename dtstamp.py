# Developed with the assistance of Microsoft Virtual Academy
# Python Fundamentals Course
# Time stamp will return the present date and time.
# Date format:
# <WEEKDAY> <MONTH> <DATE>, <YEAR>
# Time format:
# <HOURS>:<MINUTES> <AM\PM>
# Return format:
# <Date> <TIME>

import datetime


def timeStamp():
    currentDate = datetime.date.today()
    currentTime = datetime.datetime.now()
    Date = currentDate.strftime('%A %B %d, %Y')
    Time = currentTime.strftime('%I:%M %p')
    presentDT = str(Date + ' ' + Time)
    return presentDT
