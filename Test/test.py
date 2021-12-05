# coding=gbk
import re

RESULT_RE_LIST = [".*��ȷ��[:��.]?(.*)", ".*��[:��.]?(.*)", ".*��[:��.]?(.*)"]
SELECT_ITEM_RE_LIST = ["(.*)��ȷ��.*", "(.*)��.*", "(.*)��.*"]
TOPIC_CONTENT_RE_LIST = ["(.*)A[ ��.;]?.*��.*", "(.*)A[ ��.;]?.*��ȷ��.*", "(.*)A[ ��.;]?.*��.*"]

str1 = """
1.����ʮ�Ž�����ȫ�ṫ��ָ�����ڵ����쵼�£��ҹ�ʵ��������������±����㵽����С��������ȫ��С������ʷ�Կ�Խ���ƽ����л������վ��������������ΰ���Ծ����ʮ���塱�ڼ䣬�ҹ���������ˮƽ�Ȳ���ߣ������ϵ����������½�����������Ѹ����������ɫ�����ܽ�������Ʒ���������𣬾�����������Ի�������ת�䡣�ɴ˿����ƶϳ���A���������������ʹʳƷ����֧�����ϼ���B��������Ѹ�������ܴٽ����ѽṹ�����Ż�C�������ѹ���ı仯�����������Ĺؼ�����D����������Ϊ�����µľ����������ṩ����𰸣�BD
"""
for topicContent_re in TOPIC_CONTENT_RE_LIST:
    topicContent = re.search(topicContent_re, str1)
    if topicContent:
        topicContent = topicContent.group(1)
        break
print(topicContent)
topic = re.search(r"\d{1,5}[��.;]?(.*)", topicContent).group(1)
select = str1[len(topicContent):] \
            if str(str1[len(topicContent):]).startswith("A") else str1[len(topicContent) + 1:]
print(select)
# ��ȡ��ȷ�𰸲���
for result_re in RESULT_RE_LIST:
    result = re.search(result_re, select)
    if result:
        result = result.group(1)
        break
print(result)
for selectItem_re in SELECT_ITEM_RE_LIST:
    selectItem = re.search(selectItem_re, select)
    if selectItem:
        selectItem = selectItem.group(1)
        break
print(selectItem)

selectList = []
selectList_tmp = re.findall(r"[A-Z]?[.��;:��]?", selectItem)
for item in selectList_tmp:
    selectFlag = re.search(r"([A-Z]).*", item)
    if selectFlag:
        selectList.append(selectFlag.group(1))
print(selectList)

answer = []
trueCount = 0
for i in range(len(selectList)):
    selectItemData = {}
    if i == len(selectList) - 1:
        reStr = fr"{selectList[i]}(.*)"
    else:
        reStr = fr"{selectList[i]}(.*){selectList[i + 1]}"
    selectItemData['name'] = selectList[i][0]
    selectItemData['content'] = re.search(reStr, selectItem).group(1)
    selectItemData['isanswer'] = False
    if selectList[i][0] in result or result == selectList[i]:
        selectItemData['isanswer'] = True
        trueCount += 1
    answer.append(selectItemData)
print(answer)