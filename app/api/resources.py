from flask_restful import Resource, reqparse
from app.db import db_execute, db_select
import sys


class Check(Resource):
    parser_get = reqparse.RequestParser()
    parser_get.add_argument('id', required=True)

    def get(self):
        args = self.parser_get.parse_args()
        task_id = int(args['id'])
        sql_select = "SELECT status FROM tasks WHERE id=?"
        return db_select(sql_select, (task_id,)), 201
        # return "Sorry", 201


class Task(Resource):
    parser_post = reqparse.RequestParser()
    parser_post.add_argument('email')
    parser_post.add_argument('url', required=True)

    def post(self):
        #print('Hello world!', file=sys.stdout)
        args = self.parser_post.parse_args()
        sql_insert = "INSERT INTO tasks (email, url, status, MD5) VALUES (?, ?, ?, ?)"
        return db_execute(sql_insert, (
            args['email'],
            args['url'],
            1,
            '')), 201
