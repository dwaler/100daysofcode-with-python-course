from datetime import datetime
import os
import urllib.request
import re


SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, 'log')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
    logfile
)

with open(logfile) as f:
    loglines = f.readlines()

# for you to code:

def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    timestamp = re.split('\\s+', line)[1]
    return datetime.fromisoformat(timestamp)


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    all_shutdowns = [line for line in loglines if SHUTDOWN_EVENT in line]
    time_between_shutdowns = convert_to_datetime(all_shutdowns[1]) - convert_to_datetime(all_shutdowns[0])
    return time_between_shutdowns

print("Time between shutdowns:", time_between_shutdowns(loglines))
