from django.db import models

# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    parent_service = models.ForeignKey('self')
    cost = models.IntegerField()
    workflow = models.ForeignKey('Workflow')
    step_order = models.IntegerField()


class Workflow(models.Model):
    title = models.CharField(max_length=256)


class Step(models.Model):
    title = models.CharField(max_length=256)
    workflow = models.ForeignKey('Workflow')
    order = models.IntegerField()
