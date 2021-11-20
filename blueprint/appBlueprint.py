import os

from flask import request
from clear import main
from clear.tools.errorLog import getERRORLog
from .encapsulateResult import encapsulateResult
from clear.tools.errorLog import getERRORLogId
"""
    params:
        content    -> 需要清洗的内容
"""


def getBlueprint(blueprint):
    @blueprint.route("/parsing", methods=["POST"])
    def parsing():
        if request.method == "POST":
            args = request.form
            content = args.get("content")
            clearStart = main.Main()
            result = clearStart.start(content)
            logId = clearStart.getErrorLog()
            return encapsulateResult(result, logId)

    """
        params:
            file    -> 需要清洗的文件
    """

    @blueprint.route("/parsingFile", methods=["POST"])
    def parsingFile():
        if request.method == "POST":
            file = request.files['file']
            if file.filename.split(".")[1] != "txt":
                return "暂时只支持txt文本解析"
            fileDir = os.path.join("tmpData/", file.filename)
            file.save(fileDir)
            clearStart = main.Main()
            result = clearStart.startFile(fileDir)
            logId = clearStart.getErrorLog()
            os.remove(fileDir)
            return encapsulateResult(result, logId)

    @blueprint.route("/errorLog")
    def catErrorLog():
        logId = request.args.get("logId")
        return getERRORLog(logId)
