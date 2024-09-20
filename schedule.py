import calendar
import datetime as dt


def calendar_display(*args, **kwargs):
    m_input = kwargs.get('m_input')
    if m_input:
        month = m_input
    else:
        month = dt.datetime.today().month
    year = dt.datetime.today().year
    calendar.setfirstweekday(6)
    cal = calendar.month(year, month)
    return cal



