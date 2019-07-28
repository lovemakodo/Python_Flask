import os,sys
import pkgutil, importlib

def init_module(api):
    path = os.path.dirname(__file__)
    sys.path.append(path)
    modules = pkgutil.iter_modules([path])
    for module_raw in modules:
        module = importlib.import_module(module_raw.name)
        if "ns" in dir(module):
                api.add_namespace(module.ns)
    sys.path.pop()
    print("init demo resource success !")