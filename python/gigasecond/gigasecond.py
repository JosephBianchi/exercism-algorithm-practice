from datetime import datetime
from datetime import timedelta

def add_gigasecond(birth_date):
    moment = birth_date + timedelta(0, 10**9)
    return moment

print(add_gigasecond(datetime(2015, 1, 24, 23, 59, 59)))
