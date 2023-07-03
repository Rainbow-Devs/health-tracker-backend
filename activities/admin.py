from django.contrib import admin
from .models import Activity, ActivityName

# Register your models here.
admin.site.register([Activity, ActivityName])
