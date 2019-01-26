#!/usr/bin/env python3
import logging
import requests
import hashlib
from celery_conf import app
from app.db import db_execute, db_select
from .send_mail import smtp_mail


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
        md5 = hasher.hexdigest()
        db_execute(
            "UPDATE tasks SET status=?, MD5=? WHERE task_id = ?",
            (r.status_code, md5, self.request.id))
        if email:
            log.info(mail.smtp_mail(email, md5, url))
    else: 
        db_execute(
            "UPDATE tasks SET status=? WHERE task_id = ?",
            (r.status_code, self.request.id))
    return r.status_code
