import calendar
import datetime as dt


def calendar_display():
    month = dt.datetime.today().month
    year = dt.datetime.today().year

    cal = calendar.month(year, month)

    return cal
