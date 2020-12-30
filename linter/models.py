from uuid import uuid4

from django.db import models


class StatusCode(models.Model):
    code = models.PositiveIntegerField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class Code(models.Model):
    uuid = models.UUIDField(default=uuid4(), unique=True)
    session = models.DateTimeField()
    status = models.PositiveIntegerField()
    errors = models.TextField()
    statuscode = models.ForeignKey(to=StatusCode, on_delete=models.CASCADE, related_name='status_code')


    def __str__(self):
        return self.uuid