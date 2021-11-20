from .errorLog import writerERRORLog
"""
    错误处理
"""


def ClearOnERROR(topicData, result):
    if result is None:
        writerERRORLog("此题格式有问题或者没有答案，将不会被清洗出来\n" + topicData)
    else:
        return result


"""
    匹配模式没找到
"""


def NotFindClearFun(topicData):
    writerERRORLog("暂时还没适配此题的解析方式  \n" + topicData)