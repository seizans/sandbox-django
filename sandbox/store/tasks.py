# coding=utf8
from __future__ import absolute_import

from celery import shared_task
#from core.celery import app


#@app.task
@shared_task
def add(x, y):
        return x + y
