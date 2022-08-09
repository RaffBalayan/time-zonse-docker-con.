import time
from datetime import datetime
import pytz
format = "%Y-%m-%d %H:%M:%S %Z%z"
while True:
  for timeZone in pytz.all_timezones:
    time.sleep (0.5)
    now_utc = datetime.now(pytz.timezone(timeZone))
    print ("hi it is a loop",now_utc,timeZone)

