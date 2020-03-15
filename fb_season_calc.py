from datetime import datetime


now = datetime.today()


def year_calc():

    m = now.month
    y = now.year

    if m >= 10:

        y = y + 1

    return y

def season_calc():

    m = now.month
    y = now.year
    x = year_calc()
    i = y - 1

    if m >= 10:

        season = '{}-{}'.format(y, x)
    else:

        season = '{}-{}'.format(i, y)

    return season






