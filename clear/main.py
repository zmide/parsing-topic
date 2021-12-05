import re

from .startRun import getFileData, sortLineData
from clear.clearTopic.ClearLineSymbols import clearLineSymbolsASLine, clearLineSymbolsASFile
from clear.clearTopic.distinguishType import distinguishTypeASFile
from .tools.errorLog import createErrorLog


class Main:
    def __init__(self):
        self.ERRORPath = None

    def start(self, text):
        self.setErrorLog()
        self.getErrorLog()
        sortData = (clearLineSymbolsASLine(text, self.ERRORPath))
        topicData = distinguishTypeASFile(sortData)
        if topicData is None:
            return None
        for i in topicData:
            return i

    # 清洗文件开始的地方
    def startFile(self, file):
        fileData = getFileData(file)
        self.setErrorLog()
        clearData = clearLineSymbolsASFile(fileData, self.ERRORPath)
        sortData = sortLineData(clearData, True)
        topicData = distinguishTypeASFile(sortData)
        result = [item for item in topicData]
        if result is None:
            return None
        return result

    def setErrorLog(self):
        self.ERRORPath = createErrorLog()

    def getErrorLog(self):
        return re.search(r"error(\d*).log", self.ERRORPath).group(1)
