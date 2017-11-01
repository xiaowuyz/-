from datetime import datetime
from datetime import timedelta
import time


def timestamp_day( n):
    """
    返回前n天的零点时间戳
    :param n:
    :return:
    """
    data = []
    now = datetime.now().date()
    for i in range(n):
        t = now - timedelta(days=i)
        d = int(time.mktime(t.timetuple()))
        data.append(d)
    return data


def timestamp():
    """
    当前时间时间戳
    :return:
    """
    return int(time.time())


print(timestamp_day(7))