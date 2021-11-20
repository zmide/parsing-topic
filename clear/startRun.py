import json
import re
from clear.clearTopic.selectTopicClearFun import selectTypeOne, selectTypeTwo, selectTypeThree
from clear.clearTopic.BoolTopicClearFun import boolTypeOne, boolTypeTwo
from clear.tools.ClearOnERROR import ClearOnERROR, NotFindClearFun
from clear.clearTopic.FillInClearFun import FillInTypeOne


def getFileData(path):
    try:
        with open(path, "r", encoding="gbk") as f:
            lines = f.readlines()
        return lines
    except UnicodeDecodeError:
        with open(path, "r", encoding="utf8") as f:
            lines = f.readlines()
        return lines


# 将每一题设置为一行
def sortLineData(data: list, flag: bool):
    endData = []
    temporaryData = []
    for line in data:
        if re.match(r"^\d", line):
            if flag:
                flag = False
                temporaryData.append(line)
            else:
                endData.append("".join(temporaryData))
                temporaryData = [line]
        else:
            temporaryData.append(line)
    return endData


# 判断题提取
def getBoolTopicData(topicData):
    topicData = topicData.replace(" ", "")
    if re.search(r"（([√×对错])）", topicData):
        result = boolTypeOne(topicData)
        return ClearOnERROR(topicData, result)
    elif re.search(r".*答案[：][√×对错]", topicData):
        result = boolTypeTwo(topicData)
        return ClearOnERROR(topicData, result)
    else:
        NotFindClearFun(topicData)


# 选择题
def getSelectTopicData(topicData):
    topicData = topicData.replace(" ", "")
    if re.search(".*(_答案).*", topicData):
        result = selectTypeOne(topicData)
        return ClearOnERROR(topicData, result)
    elif re.search(r"(.*)A[、.;:]?.*答案|正确答案.*", topicData):
        result = selectTypeTwo(topicData)
        return ClearOnERROR(topicData, result)
    elif re.search(r"（([A-Z])）", topicData):
        result = selectTypeThree(topicData)
        return ClearOnERROR(topicData, result)
    else:
        NotFindClearFun(topicData)


# 填空题
def getFillInTopicData(topicData):
    if re.search(".*答案[:：](.*)", topicData):
        result = FillInTypeOne(topicData)
        return ClearOnERROR(topicData, result)
    else:
        NotFindClearFun(topicData)


# 保存数据为Json
def saveDataToJson(data, path):
    endResult = []
    for topic in data:
        if topic:
            endResult.append(topic)
    file = open(path, "w+", encoding="utf8")
    json.dump(endResult, file, ensure_ascii=False, indent=4)




