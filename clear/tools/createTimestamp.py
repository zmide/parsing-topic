import time

"""
    生成一个时间戳
"""


def createTimestamp():
    return str(int(time.time() * 10000))
