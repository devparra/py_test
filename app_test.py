############################
# Python Sandbox version 1 #
############################


# The OS module provides dozens of functions for interacting with an OS
import os
import sys, getopt
# use the shutil for shell utilities, interacting with the os
import shutil
# The re module provides regular expression tools
import re
# Supports various math functions in the C Library
import math
# Random module provides tools for making random selections
import random
# For basic statistical calculation properties (mean, median, variance)
import statistics
# Providing libraries for internet access
from urllib.request import urlopen
# used to send smtp messages to other devices
import smtplib
# One of many compression libraries
import zlib
# For latency testing
from timeit import Timer
# For docstring testing
import doctest
# Unittest for class defined tests
import unittest
# Library for abbreviated displays of large or deeply nested containers
import reprlib
# The textwrap module formats paragraphs of text to fit a given screen width
import textwrap
# The locale module accesses a database of culture specific data formats.
# The grouping attribute of locales format function provides a direct way
# of formatting numbers with group separators
import locale
# The string module allows for templating of data outputs using $<keyword>
from string import Template
# used for file renaming, the time module will supply a time stamp. os.path
# will provide the current path
import time
import os.path
# The struct module provides pack() and unpack() functions for working with
# variable length binary record formats.
import struct
# Threading is used to run tasks in background while the main program continues
import threading
# for ziping files (simple file compression)
import zipfile
# The weakref module provides tools for tracking objects without creating a reference.
import weakref, gc
# The array module provides an array() object that is like a list that stores only
# homogeneous data and stores it more compactly.
from array import array
# The collections module provides a deque() object that is like a list with
# faster appends and pops from the left side but slower lookups in the middle
from collections import deque
# The bisect module with functions for manipulating sorted lists
import bisect
# The heapq module provides functions for implementing heaps based on regular
# lists. The lowest valued entry is always kept at position zero.
from heapq import heapify, heappop, heappush
# The decimal module offers a Decimal datatype for decimal floating point arithmetic
from decimal import *
# Provides date time stamp
import dtstamp

# Classes

# Global functions
# This will connect to the internet/website


# HackerRank leap year challenge
# A leap year is evenly divisible by 4, but is not a leap year if divisible by 100
# unless it is divisible by 400.
# 1800 < X
# def is_leap(year):
#     leap = False
#     if year % 4 == 0:
#         if year % 100 != 0 or year % 400 == 0:
#             leap = True
#     return print(leap)


# Main application
def test_bot():
    error_flag = False
    try:
        # Leap year output
        # year = int(input())
        # is_leap(year)
        # print(year % 4)
        # print(year % 100)
        # print(year % 400)

        # something to do
        print(time.ctime())


    except Exception:
        error = str(sys.exc_info()[1])
        log_file = 'errorlog.txt'
        append = 'a'
        date = dtstamp.timeStamp()
        with open(log_file, mode=append) as log_entery:
            log_entery.write('\n' + error + ' ' + date)
            log_entery.close()
        error_flag = True
        print('Oops! Something went wrong.')
        print(date + ' ' + error)
    if not error_flag:
        date = dtstamp.timeStamp()
        print('\n' + date + '\nThank you.\n')
    return


if __name__ == '__main__':
    test_bot()
    # print function
    n = int(input())
    x = []
    for i in range(n+1):
        if i == 0:
            pass
        if i > 0:
            x.append(i)
        if i == n:
            # print(*x, sep=' ', end='\n', file=sys.stdout)
            print(*x, sep='')
