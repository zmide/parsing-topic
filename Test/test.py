# coding=gbk
import re

RESULT_RE_LIST = [".*正确答案[:：.]?(.*)", ".*答案[:：.]?(.*)", ".*答[:：.]?(.*)"]
SELECT_ITEM_RE_LIST = ["(.*)正确答案.*", "(.*)答案.*", "(.*)答.*"]
TOPIC_CONTENT_RE_LIST = ["(.*)A[ 、.;]?.*答案.*", "(.*)A[ 、.;]?.*正确答案.*", "(.*)A[ 、.;]?.*答.*"]

str1 = """
1.党的十九届六中全会公报指出，在党的领导下，我国实现了人民生活从温饱不足到总体小康、奔向全面小康的历史性跨越，推进了中华民族从站起来到富起来的伟大飞跃。“十三五”期间，我国居民收入水平稳步提高，恩格尔系数整体持续下降，服务消费迅速增长，绿色、智能健康类商品销售日益红火，居民消费向个性化多样化转变。由此可以推断出会A居民收入持续增长使食品消费支出不断减少B服务消费迅速增长能促进消费结构不断优化C居民消费观念的变化是消费升级的关键因素D消费升级能为塑造新的经济增长点提供引领答案：BD
"""
for topicContent_re in TOPIC_CONTENT_RE_LIST:
    topicContent = re.search(topicContent_re, str1)
    if topicContent:
        topicContent = topicContent.group(1)
        break
print(topicContent)
topic = re.search(r"\d{1,5}[、.;]?(.*)", topicContent).group(1)
select = str1[len(topicContent):] \
            if str(str1[len(topicContent):]).startswith("A") else str1[len(topicContent) + 1:]
print(select)
# 获取正确答案部分
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
selectList_tmp = re.findall(r"[A-Z]?[.、;:：]?", selectItem)
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