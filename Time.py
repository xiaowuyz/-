from datetime import datetime
from datetime import timedelta
import time


def timestamp_day(l=0, r=1):
    """
    :param l:从l开始
    :param r:到r结束，r不包括
    :return:l-r天的零点时间戳，list
    """
    data = []
    now = datetime.now().date()
    for i in range(l, r):
        t = now + timedelta(days=-i)
        d = int(time.mktime(t.timetuple()))
        data.append(d)
    return data


def timestamp():
    """
    当前时间时间戳
    :return:
    """
    return int(time.time())