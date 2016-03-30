from django.db import models
from main.components.sms import NetScSmsClient

# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    parent_service = models.ForeignKey('self', blank=True, null=True, default=0)
    cost = models.IntegerField()
    workflow = models.ForeignKey('Workflow')

    def __str__(self):
        return self.title

    def get_tree(self, include_self=True):
        r = []
        if include_self:
            r.append(self)
        for c in Service.objects.filter(parent_service=self):
            r.append({self: c.get_tree(include_self=False)})
            return r


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
    step_order = models.IntegerField(default=0)

    def __str__(self):
        return self.id.__str__()


class SubOrder(models.Model):
    order = models.ForeignKey('Order')
    service = models.ForeignKey('Service')
    description = models.TextField()


class WorkflowLog(models.Model):
    order = models.ForeignKey('Order')
    step_move = models.ForeignKey('StepMove')
    description = models.TextField('Step')
    created = models.DateTimeField(auto_now_add=True)

    def save(self):
        if self.fk is None:
            sms_client = NetScSmsClient()
            sms_client.send_sms(['9136496628'], self.step_move.message)
        super(models.Model, self).save()


class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    address = models.TextField()
    postal_code = models.CharField(max_length=16)
    phone = models.CharField(max_length=16)
    is_confirmed = models.BooleanField(default=False)
    balance = models.IntegerField(default=0)


class StepMove(models.Model):
    title = models.CharField(max_length=256, default='')
    order = models.ForeignKey('Order', default=0)
    into_step = models.ForeignKey('Step', related_name='from_step_move_set')
    from_step = models.ForeignKey('Step', related_name='into_step_move_set')
    message = models.TextField()
    user_groups = models.ManyToManyField('auth.Group')
