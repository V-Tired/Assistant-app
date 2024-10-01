import calendar
import datetime as dt

"""Use python's calendar module to display a text-line calendar. Optionally take m_input to specify which month,
otherwise default to current month."""


def calendar_display(*args, **kwargs) -> str:

    m_input = kwargs.get('m_input')
    if m_input:
        month = m_input
    else:
        month = dt.datetime.today().month
    year = dt.datetime.today().year
    calendar.setfirstweekday(6)
    cal = calendar.month(year, month)
    return cal



