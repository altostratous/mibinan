from django.db import models

# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    parent_service = models.ForeignKey('self', blank=True, null=True, default=0)
    cost = models.IntegerField()
    workflow = models.ForeignKey('Workflow')

    def __str__(self):
        return self.title


class Workflow(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class Step(models.Model):
    title = models.CharField(max_length=256)
    workflow = models.ForeignKey('Workflow')
    order = models.IntegerField()

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey('auth.User')
    created = models.DateTimeField(auto_now_add=True)
    service_set = models.ManyToManyField("Service")
    step_order = models.IntegerField(default=0)

    def __str__(self):
        return self.id
