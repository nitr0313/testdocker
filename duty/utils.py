from datetime import date, datetime, timedelta
from . import models


def gen(st_day, entr, revers=False):
    if revers:
        flats = models.Flat.objects.all().filter(entrance=entr).order_by("-number")
    else:
        flats = models.Flat.objects.all().filter(entrance=entr).order_by("number")

    dlt1 = timedelta(days=1)
    dlt6 = timedelta(days=6)
    color = ('white', '#d0d07a')
    for flat in flats:
        if flat.active:
            flat.date_duty_start = st_day
            flat.date_duty_finish = st_day + dlt6
            st_day = st_day + dlt6 + dlt1
        flat.background = color[int(flat.number) % 2]

    return flats
