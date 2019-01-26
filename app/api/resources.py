from flask_restful import Resource, reqparse
from app.db import db_execute, db_select
from app.task_processing.task_executer import add_task


def make_responce(sql_row):
    rec = {}
    if sql_row is None:
        rec['error'] = "unknown identifier"
    elif sql_row[0] == 200:
        rec['md5'] = sql_row[1]
        rec['status'] = "done"
        rec['url'] = sql_row[2]
    elif sql_row[0] == 100:
        rec['status'] = 'running'
    else:
        rec['status'] = sql_row[0]
    return rec


class Check(Resource):
    parser_get = reqparse.RequestParser()
    parser_get.add_argument('id', required=True)

    def get(self):
        args = self.parser_get.parse_args()
        task_id = args['id']
        sql_select = "SELECT status, MD5, url FROM tasks WHERE task_id=?"
        ans = db_select(sql_select, (task_id,))
        return make_responce(ans)


class Task(Resource):
    parser_post = reqparse.RequestParser()
    parser_post.add_argument('email')
    parser_post.add_argument('url', required=True)

    def post(self):
        args = self.parser_post.parse_args()
        task_id = add_task(
            url=args['url'], email=args['email'])
        sql_insert = "INSERT INTO tasks (email, url, task_id, status, MD5) VALUES (?, ?, ?, ?, ?)"
        db_execute(sql_insert, (
            args['email'],
            args['url'],
            task_id,
            100,
            '')), 201
        return {"id": task_id}
