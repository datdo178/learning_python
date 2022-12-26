"""
Link: https://docs.python.org/3/library/datetime.html
"""

import _datetime
from _datetime import date

# Constants
print('Constants:')
print('MINYEAR', _datetime.MINYEAR)
print('MAXYEAR', _datetime.MAXYEAR)

# Declare date, time:
today = date.today()
yesterday = date(2022, 10, 11)
tomorrow = date.fromisoformat('2022-10-13')
time_stamp = date.fromtimestamp(1666587143)  # 2022-10-24

print(today)
print(today.year)
print(today.month)
print(today.day)

# Check isDate
isDate = isinstance(yesterday, date)
