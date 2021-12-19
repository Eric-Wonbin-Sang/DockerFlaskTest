import datetime

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {
            "time_of_request": datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
            "hello": "world"
        }


api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run(debug=True)
