import time
from datetime import datetime


n = 5


def time_now():
    time.sleep(1)
    a = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S:")
    return a


res = [time_now() for i in range(n)]
print(res)
