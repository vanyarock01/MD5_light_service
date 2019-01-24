from flask_restful import Resource, reqparse

parser_get = reqparse.RequestParser()
parser_get.add_argument('id', required=True)


class Check(Resource):

    def get(self):
        args = parser_get.parse_args()
        task_id = int(args['id'])
        return TASKS[task_id]['status'], 201


parser_post = reqparse.RequestParser()
parser_post.add_argument('email')
parser_post.add_argument('url', required=True)


class Task(Resource):

    def post(self):
        args = parser_post.parse_args()
        task_id = generate_id()
        TASKS[task_id] = {
            'email': args['email'],
            'url': args['url'],
            'status': 'running'}
        return task_id, 201
