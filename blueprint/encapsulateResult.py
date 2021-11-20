def encapsulateResult(result, logId):
    endResult = {"code": 200, "logId": logId, "content": result}
    if result is None:
        endResult["code"] = 300
        endResult["content"] = "解析错误，请通过logId了解更多"
    return endResult
