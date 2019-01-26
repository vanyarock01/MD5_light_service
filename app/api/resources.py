from flask_restful import Resource, reqparse
from app.db import db_execute, db_select
from app.task_processing.task_executer import add_task


class Check(Resource):
    parser_get = reqparse.RequestParser()
    parser_get.add_argument('id', required=True)

    def get(self):
        args = self.parser_get.parse_args()
        task_id = args['id']
        sql_select = "SELECT status, MD5, url FROM tasks WHERE task_id=?"
        ans = db_select(sql_select, (task_id,))

        if ans is None:
            result = {"error": "unknown identifier"}
        elif ans[0] == 200:
            result = {
                "md5": ans[1],
                "status": "done",
                "url": ans[2]}
        elif ans[0] == 100:
            result = {
                "status": "running"}
        else:
            result = {
                "status": ans[0]}
        return result


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
