from my_module import find_index as fi, test
import sys
import random
import math
import datetime
import calendar
import os

courses = ['History', 'Math', 'Physics', 'CompSci']

print(fi(courses, 'Physics'))
print(test)
print(sys.path)
print(random.choice(courses))
rads = math.radians(90)
print(math.sin(rads))

print(datetime.date.today())

print(calendar.isleap(2017))
print(calendar.isleap(2020))
print(os.getcwd())