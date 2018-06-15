# -*- coding:UTF-8 -*-

import time

year = raw_input("Year?")
month = int(raw_input("Month?"))
day = raw_input("day?")

amonth = ("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")
input_day = amonth[month-1]+" "+day+" "+year
otime = time.mktime(time.strptime(input_day,"%b %d %Y"))
ltime = time.localtime(otime)
print ltime
print time.strftime("%j",ltime)