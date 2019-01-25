from __future__ import absolute_import, unicode_literals
from celery import Celery


app = Celery('transfer_learning',
             broker='redis://',
             backend='redis://',
             include=[
                 'app.task_processing.task_executer',
             ])

app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
    CELERY_TASK_SERIALIZER='pickle',
    CELERY_RESULT_SERIALIZER='pickle',
    CELERY_ACCEPT_CONTENT=['pickle', 'json']
)

if __name__ == '__main__':
    app.start()
