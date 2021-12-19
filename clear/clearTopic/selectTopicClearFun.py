"""
    第一中选择题类型
    答案跟着选项后面，如：
    A、xxxx_答案
"""
import re


def selectTypeOne(topicData):
    selectContentItem = {}
    try:
        # 提取题目部分
        selectTopic = re.findall(r"(.*)A[、.;]?", topicData)
        # print(selectTopic)
        selectResult = topicData[len(selectTopic[0]):]
        # 提取选项
        select = re.findall(r"([A-Z]?[、.])", selectResult)
        answer = []
        selectTrueNum = 0
        content = re.search("^\d{1,3}[、.]?(.*)", selectTopic[0]).group(1)
        for i in range(len(select)):
            selectItemData = {}
            if i == len(select) - 1:
                reStr = fr"{select[i]}(.*)"
            else:
                reStr = fr"{select[i]}(.*){select[i + 1]}"
            selectContent = re.findall(reStr, selectResult)[0]
            selectItemData["name"] = select[i][0]
            selectItemData["content"] = selectContent
            selectItemData["isanswer"] = False
            if "_答案" in selectContent:
                selectItemData["content"] = selectContent.split("_答案")[0]
                selectItemData["isanswer"] = True
                selectTrueNum += 1
            answer.append(selectItemData)
        answer.append(selectTrueNum)
        if selectTrueNum == 0:
            return None
        return encloseResult(content, answer)
    except Exception:
        return None


"""
    第二中选择题类型
    答案跟着题干后面，如：
    D、xxxxxxxxxxxxxxxxxxxxxx答案:A
    
    topic  -> 最后的题目
    answer  -> 最后的答案
"""

RESULT_RE_LIST = [".*正确答案[:：.]?(.*)", ".*答案[:：.]?(.*)", ".*答[:：.]?(.*)", ]
SELECT_ITEM_RE_LIST = ["(.*)正确答案.*", "(.*)答案.*", "(.*)答.*"]
TOPIC_CONTENT_RE_LIST = ["(.*)A[ 、.;]?.*答案.*", "(.*)A[ 、.;]?.*正确答案.*", "(.*)A[ 、.;]?.*答.*"]


def selectTypeTwo(topicData):
    try:
        for topicContent_re in TOPIC_CONTENT_RE_LIST:
            topicContent = re.search(topicContent_re, topicData)
            if topicContent:
                topicContent = topicContent.group(1)
                break

        topic = re.search(r"\d{1,5}[、.;]?(.*)", topicContent).group(1)
        select = topicData[len(topicContent):]
        # 获取正确答案部分
        for result_re in RESULT_RE_LIST:
            result = re.search(result_re, select)
            if result:
                result = result.group(1)
                break
        for selectItem_re in SELECT_ITEM_RE_LIST:
            selectItem = re.search(selectItem_re, select)
            if selectItem:
                selectItem = selectItem.group(1)
                break

        selectList = []
        selectList_tmp = re.findall(r"[A-Z]?[.、;:：]?", selectItem)
        for item in selectList_tmp:
            selectFlag = re.search(r"([A-Z]).*", item)
            if selectFlag:
                selectList.append(selectFlag.group(1))
        # if selectList is None:
        #     return None
        answer = getSelectItemContent(selectItem, selectList, result)
        # print(selectList)
        if not answer:
            return None
        return encloseResult(topic, answer)
    except AttributeError:
        # return None
        print(AttributeError)
    # except TypeError:
    #     print(topicData)


"""
    第二中选择题类型
    答案跟着题干中，如：
    D、xxxxxxxxxxxxxx(A)xxxxxxxx

    topic  -> 最后的题目
    answer  -> 最后的答案
"""


def selectTypeThree(topicData):
    try:
        topic = re.search("(.*)A[.、]?", topicData).group(1)
        selectItem = topicData[len(topic):]
        topic = re.search("^\d{1,5}[.:：、]?(.*)", topic).group(1)
        result = re.search(".*（([A-Z])", topic).group(1)
        newTopic = re.sub("（([A-Z])）", "（  ）", topic)
        allSelectContent = re.findall(r"[A-Z][.、;:：]?", selectItem)
        allSelectContent = allSelectContent[0:5] if len(allSelectContent) > 5 else allSelectContent
        answer = getSelectItemContent(selectItem, allSelectContent, result)
        if answer is None:
            return None
        return encloseResult(newTopic, answer)
    except Exception:
        return None


"""
    :type
    获取选项的内容
        allSelectContent    -> 所有选项的内容
        selectList          -> 选项
        result              -> 结果
    return  -> 封装好的选项和答案个数          
"""


def getSelectItemContent(allSelectContent, selectList, result):
    try:
        answer = []
        trueCount = 0
        for i in range(len(selectList)):
            selectItemData = {}
            if i == len(selectList) - 1:
                reStr = fr"{selectList[i]}(.*)"
            else:
                reStr = fr"{selectList[i]}(.*){selectList[i + 1]}"
            selectItemData['name'] = selectList[i][0]
            selectItemData['content'] = re.search(reStr, allSelectContent).group(1)
            selectItemData['isanswer'] = False
            if selectList[i][0] in result or result == selectList[i]:
                selectItemData['isanswer'] = True
                trueCount += 1
            answer.append(selectItemData)
        if trueCount == 0:
            return None
        answer.append(trueCount)
        return answer
    except Exception:
        return None


"""
    封装结果
    topicContent    -> 题干
    topicResult     -> 结果
"""


def encloseResult(topicContent, topicResult):
    result = {"type": 0, "id": 0, "name": "单选题", "content": topicContent, "answer": topicResult[:-1]}
    if topicResult[-1] > 1:
        result['name'] = "多选题"
        result['type'] = 1
    return result
