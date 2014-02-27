# coding=utf8

from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    author = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField(null=False, blank=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
