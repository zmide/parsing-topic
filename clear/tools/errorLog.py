import re

from .createTimestamp import createTimestamp
import os
import time

ERRORPath = ""

"""
    生成错误日志文件
"""


def createErrorLog():
    timestamp = createTimestamp()
    global ERRORPath
    ERRORPath = os.path.join("logs", "error" + timestamp + ".log")
    uselessFile = open(ERRORPath, "a+", encoding="utf8")
    nowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    uselessFile.write(f"-----------------------------{nowTime} 进行了一次清洗----------------------------- \n \t其中被无用数据有如下:\n")
    return ERRORPath


"""
    往错误日志文件里写入内容
"""


def writerERRORLog(error):
    log = open(ERRORPath, "a+", encoding="utf8")
    log.write(error)
    log.close()


"""
    获取错误日志文件
"""


def getERRORLog(logId):
    log = ""
    logPath = os.path.join("logs", "error"+logId+".log")
    with open(logPath, "r", encoding="utf8") as fp:
        for line in fp.readlines():
            log += line
    # removeERRORLog(logPath)
    return log


"""
    删除错误日志文件
"""


def removeERRORLog(logPath):
    os.remove(logPath)


def getERRORLogId():
    return ERRORPath