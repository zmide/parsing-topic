import json


def encapsulateResult(result, logId):
    endResult = json.dumps({"code": 200, "logId": logId, "content": result}, ensure_ascii=False)
    if result is None:
        endResult["code"] = 300
        endResult["content"] = "解析错误，请通过logId了解更多"
    return endResult
