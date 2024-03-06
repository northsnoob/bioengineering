
import datetime

def epoch2datetime(epochtime):
    offset_hours = 8 # UTC+8
    return datetime.datetime.utcfromtimestamp(epochtime) + datetime.timedelta(hours=offset_hours)
