from flask_restplus import Namespace
from app import api

ns = Namespace("view")
api.add_namespace(ns)

@ns.route("/")
def get_user():
    print("jinyilun")
    return "yes sucess"