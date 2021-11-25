from clear.startRun import *

""":type

"""


# 区分一批题目类型
def distinguishTypeASFile(data: list):
    for topic in data:
        if re.match(r".*([A-Z][、.:]?)", topic.replace(" ", "")):
            yield getSelectTopicData(topic)
        elif re.search(r"（([√×])）|（([对错])）| .*答案：[对错]", topic.replace(" ", "")):
            yield getBoolTopicData(topic)
        else:
            yield getFillInTopicData(topic)


# # 区分一个题目类型
# def distinguishTypeASLine(data):
#     if re.match(r".*([A-Z][、.:]?)", data):
#         yield getSelectTopicData(data)
#     elif re.search(r"（([√×])）|（([对错])）|.*答案：[对错]", data):
#         yield getBoolTopicData(data)
#     else:
#         yield getFillInTopicData(data)