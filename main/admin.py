from django.contrib import admin
from django.contrib.auth.models import *
from .models import *

# Register your models here.
admin.site.register(Service)
admin.site.register(Workflow)
admin.site.register(Step)
admin.site.register(Order)
admin.site.register(Profile)
admin.site.register(Permission)
