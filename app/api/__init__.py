from flask import Blueprint
from flask_restplus import Api, Resource
import os, sys
import pkgutil, importlib

blueprint = Blueprint("app", "app BP", url_prefix="/app")
api = Api(blueprint, version="1.0", title="app", description="the app API")

@api.route("/test")
class test(Resource):
    def get(self):
        return "test"

def init_module(app):
    path = os.path.dirname(__file__)
    sys.path.append(path)
    modules = pkgutil.iter_modules([path])
    for module_raw in modules:
        if module_raw.ispkg:
            module = importlib.import_module(module_raw.name)
            if "init_module" in dir(module):
                module.init_module(api)
    app.register_blueprint(blueprint)
    sys.path.pop()
    print("init api Success!")