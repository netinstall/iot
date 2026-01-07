import datetime
from dateutil import tz
from suntime import Sun, SunTimeException
from settings import SUN_LAT, SUN_LON, SUN_TZNAME

def is_dark():
    sun = Sun(SUN_LAT, SUN_LON)
    now_dt = datetime.datetime.now().replace(tzinfo=tz.gettz(SUN_TZNAME))
    sunset_dt = sun.get_local_sunset_time(datetime.datetime.now(),tz.gettz(SUN_TZNAME))
    sunrise_dt = sun.get_local_sunrise_time(datetime.datetime.now(),tz.gettz(SUN_TZNAME))

    return not (sunrise_dt <= now_dt <= sunset_dt)
