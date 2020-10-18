#!/usr/bin/env python3
import time
from datetime import datetime

# Añade al fichero la fecha y hora actual
var = datetime.now()
f = open("pythontime.txt","a+")
f.write("fecha %s \n " % var)
f.close()
