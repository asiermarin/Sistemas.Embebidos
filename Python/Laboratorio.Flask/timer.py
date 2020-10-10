#!/usr/bin/env python3
import sys
import time 

class Timer:

    def __init__(self, seconds):
        self.seconds = seconds
        self.__export_seconds_every_second(seconds)

    def __export_seconds_every_second(self, seconds):
        temporize = time.time()
        value_to_print = 1
        difference = 0.0
        while (difference <= seconds):
            time_until_this = time.time()
            difference = time_until_this - temporize
            if (value_to_print < difference):
                value_to_print = value_to_print + 1
                print(difference)

if __name__ == '__main__':
    # x = Timer(sys.argv[1]) # The value by: ./timer.py [sys.argv[1]]...[sys.argv[2]]
    x = Timer(5.0) # To TEST