from flask import Flask
import pkgutil, os
import importlib

app = Flask("DomeApp")

def init_module(app):
    path = os.getcwd()
    modules = pkgutil.iter_modules([path])
    for module_raw in modules:
        if module_raw.ispkg:
            module = importlib.import_module(module_raw.name)
            if "init_module" in dir(module):
                module.init_module(app)

if __name__ == "__main__":
    init_module(app)