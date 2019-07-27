from flask_restplus import Api
from flask import Blueprint

blueprint = Blueprint("app", "app BP", url_prefix="/app")
api = Api(blueprint, version="1.0", title="app", description="the app API")

def init_module(app):
    print("init app.init_module")
    api.init_app(app)

