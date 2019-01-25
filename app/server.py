from flask import Flask, request
from flask_restful import abort, Api, Resource

from app.api import Task
from app.api import Check

app = Flask(__name__)
api = Api(app)

api.add_resource(Task, '/sumbit')
api.add_resource(Check, '/check')


def run_app(*args, **kwargs):
    app.run(*args, **kwargs)


if __name__ == '__main__':
    run_app(debug=True)
