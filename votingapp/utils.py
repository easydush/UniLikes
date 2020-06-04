import datetime as dt


def get_semester(adm_year):
    today = dt.datetime.today().date()
    adm_day = dt.date(adm_year, 9, 1)
    delta = today - adm_day
    semester = (delta.days // 365 + 1) * 2
    if delta.days < 183:
        semester -= 1
    return semester
