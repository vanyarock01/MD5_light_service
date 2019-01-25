import logging
import requests
import hashlib
from celery_conf import app
from app.db import db_execute, db_select


FORMAT = '%(levelname)-8s %(asctime)-15s %(name)-10s %(funcName)-10s %(lineno)-4d %(message)s'
logging.basicConfig(format=FORMAT)
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


def add_task(url, email=''):
    process = calculate_task.apply_async((url, email))
    log.info("Task added.\n")
    return process.task_id


@app.task(ignore_result=True, bind=True)
def calculate_task(self, url, email=''):
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        hasher = hashlib.md5()
        hasher.update(r.content)
        sql = "UPDATE tasks SET status=?, MD5=? WHERE task_id = ?"
        db_execute(
            sql, (r.status_code, hasher.hexdigest(), self.request.id))

    return r.status_code
