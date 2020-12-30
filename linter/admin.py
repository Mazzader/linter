from django.contrib import admin

from .models import StatusCode, Code

admin.site.register(StatusCode)
admin.site.register(Code)