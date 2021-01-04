from uuid import uuid4

from django.db import models
from datetime import datetime

import os


class StatusCode(models.Model):
    code = models.PositiveIntegerField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class Code(models.Model):
    uuid = models.UUIDField(default=uuid4(), unique=True)
    session = models.DateTimeField(default=datetime.now())
    status = models.PositiveIntegerField()
    errors = models.TextField()
    statuscode = models.ForeignKey(to=StatusCode, on_delete=models.CASCADE, related_name='status_code')

    def __str__(self):
        return str(self.uuid)


class Document(models.Model):
    docfile = models.FileField(upload_to='documents')


class DocumentEntry(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    field = models.CharField(max_length=250, default="TEST")
