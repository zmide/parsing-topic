
"""
    第一种填空题类型
        答案在最后面
        例如：1、判处罚金，应当根据     决定罚金数额。答案：犯罪情节
"""
import re


def FillInTypeOne(topicData):
    try:
        content = re.search(r"(.*)答案[：:](.*)", topicData)
        topic = re.search(r"\d{1,5}[、.;]?(.*)", content.group(1)).group(1)
        result = content.group(2)
        if not result:
            return None
        return encloseResult(topic, result)
    except Exception:
        return None


"""
    封装题目
        topicContent -> 题干
        topicResult  -> 答案
"""


def encloseResult(topicContent, topicResult):
    return {"content": topicContent, "type": 2, "id": 0, "name": "填空题", "answer": topicResult}
