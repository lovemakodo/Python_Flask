import os, sys
import pkgutil, importlib


def init_module(app):
    path = os.path.dirname(__file__)
    sys.path.append(path)
    modules = pkgutil.iter_modules([path])
    for module_raw in modules:
        if module_raw.ispkg:
            module = importlib.import_module(module_raw.name)
            if "init_module" in dir(module):
                module.init_module(app)
    sys.path.pop()
    print("app init Success!")

