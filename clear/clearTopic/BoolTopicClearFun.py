"""
    第一种类型：
        答案在题目的括号中
        例如: 1.xxxxxxxxxxxxx(对|√)
"""
import re


def boolTypeOne(topicData):
    try:
        resultGroupData = re.search(r"（([√×])）|（([对错])）", topicData)
        if resultGroupData.group(1) is None:
            result = resultGroupData.group(2)
        else:
            result = resultGroupData.group(1)
        newTopic = re.search("^\d{1,3}[、.]?(.*)", re.sub(r"（([√×])）|（([对错])）", "（  ）", topicData)).group(1)
        resultData = encloseResult(newTopic, result)
        if resultData:
            return resultData
        else:
            return None
    except AttributeError:
        return None


"""
    TODO 第二种类型：
        答案在题目的最后面：
        例如：1.xxxxxxxxxxx()xxxx。答案：对/√
"""


def boolTypeTwo(topicData):
    try:
        newTopic = re.search("^\d{1,3}[、.]?(.*)", re.search(r"(.*)答案.*", topicData).group(1)).group(1)
        result = re.search(r".*答案.?([对错√×])", topicData).group(1)
        resultData = encloseResult(newTopic, result)
        if resultData:
            return resultData
        else:
            return None
    except AttributeError:
        return None


"""
    TODO 第二种类型：
        答案在题目的最后面：
        例如：1.xxxxxxxxxxx()xxxx。答案：对/√
"""


def boolTypeThree(topicData):
    try:
        newTopic = re.search("^\d{1,3}[、.]?(.*)", topicData[:-1]).group(1)
        result = topicData[-1]
        resultData = encloseResult(newTopic, result)
        # print(resultData)
        if resultData:
            return resultData
        else:
            return None
    except AttributeError:
        return None


"""
    封装结果
        topicContent -> 题干
        topicResult -> 答案
"""


def encloseResult(topicContent, topicResult):
    selectContentItem = {"content": topicContent, "type": 3, "id": 0, "name": "判断题"}
    if topicResult == "√" or topicResult == "对":
        selectContentItem["answer"] = True
    if topicResult == "×" or topicResult == "错":
        selectContentItem["answer"] = False
    if not topicResult:
        return None
    return selectContentItem
