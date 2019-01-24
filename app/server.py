from flask import Flask, request
from flask_restful import abort, Api, Resource

from app.api import Task
from app.api import Check

app = Flask(__name__)
api = Api(app)

TASKS = {}


class ServiceApp(object):

    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)

        self.api.add_resource(Task, '/sumbit')
        self.api.add_resource(Check, '/check')

    def run(self, *args, **kwargs):
        self.app.run(*args, **kwargs)


def run_app(*args, **kwargs):
    app = ServiceApp()
    app.run(*args, **kwargs)

if __name__ == '__main__':
    run_app(debug=True)
