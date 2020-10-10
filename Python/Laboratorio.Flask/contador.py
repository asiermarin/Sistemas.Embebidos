#!/usr/bin/env python3
import sys
import time 
from time import sleep 
from datetime import datetime

class Contador:

    _time = None
    _STOP_CHARACTER = 'Q'

    def __init__(self):
        self._time = time.time()
        self.__stop()

    def __stop(self):
        stop_string = None
        while(stop_string != self._STOP_CHARACTER):
            stop_string = input("Enter 'Q' if you want to stop: ")
        last_time = time.time()
        print(last_time - self._time)

if __name__ == '__main__':
    # x = Timer(sys.argv[1]) # The value by: ./contador.py [sys.argv[1]]...[sys.argv[2]]
    x = Contador() # To TEST