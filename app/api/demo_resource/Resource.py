from flask_restplus import Namespace, Resource

ns = Namespace("demo")

@ns.route("")
class demo_root(Resource):
    def get(self):
        print("this is demo root")
        return "demo root success!"
