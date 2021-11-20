from flask import Blueprint
from . import appBlueprint

blueprintApp = Blueprint("app", __name__)
appBlueprint.getBlueprint(blueprintApp)