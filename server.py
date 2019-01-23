from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

TASKS = {}


def abort_if_todo_doesnt_exist(task_id):
    if task_id not in TASKS:
        abort(
            404, message="Todo {} doesn't exist".format(task_id))

parser = reqparse.RequestParser()
parser.add_argument('email')
parser.add_argument('url')


def generate_id():
    return len(TASKS)


class Task(Resource):

    def get(self):
        return Task

    def post(self):
        args = parser.parse_args()
        task_id = generate_id()
        TASKS[task_id] = {
            'email': args['email'],
            'url': args['url']}
        return task_id, 201


api.add_resource(Task, '/sumbit')

if __name__ == '__main__':
    app.run(debug=True)
