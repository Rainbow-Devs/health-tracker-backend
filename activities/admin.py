from django.contrib import admin
from .models import Activities, ActivityTypes

# Register your models here.
admin.site.register([Activities, ActivityTypes])
