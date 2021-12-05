import time
import re

"""
    清洗一个文件数据的方法
    data            -> 文件组成的list
    清理掉每行中的特殊内容 判断需要留下的数据内容

"""


def clearLineSymbolsASFile(data: list, ERRORPath):
    uselessFile = open(ERRORPath, "a+", encoding="utf8")
    newData = []
    for line in data:
        newLine = line.replace("\n", "").replace("\t", "") \
            .replace("\u3000", "").replace("\xa0", "") \
            .replace("(", "（").replace(")", "）").replace("．", ".").replace("ⅹ", "×")
        if re.match("^\d|^[A-G]|^答案|^正确答案|①|②|③|④|⑤|⑥|（1）|（2）|（3）|（4）|（5）|（6）|^答", newLine):
            newData.append(newLine)
        else:
            if line.replace("\n", "").replace(" ", ""):
                uselessFile.write(newLine + "\n")
    uselessFile.close()
    return newData


"""
    清洗单行数据的方法
    
"""


def clearLineSymbolsASLine(data: str, ERRORPath):
    uselessFile = open(ERRORPath, "a+", encoding="utf8")
    newData = []
    newLine = data.replace("\n", "").replace("\t", "") \
        .replace("\u3000", "").replace("\xa0", "") \
        .replace("(", "（").replace(")", "）").replace(" ", "")
    if re.match("^\d|^[A-G]|^答案|^正确答案", newLine):
        newData.append(newLine)
    else:
        if data.replace("\n", "").replace(" ", ""):
            uselessFile.write(newLine + "\n")
    uselessFile.close()
    return newData
