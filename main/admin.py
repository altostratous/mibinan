from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Service)
admin.site.register(Workflow)
admin.site.register(Step)
admin.site.register(Order)
admin.site.register(Profile)
