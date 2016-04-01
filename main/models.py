from django.db import models
from main.components.sms import NetScSmsClient

# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    parent_service = models.ForeignKey('self', blank=True, null=True, default=0)
    cost = models.IntegerField()
    workflow = models.ForeignKey('Workflow')
    is_countable = models.BooleanField(default=False)
    is_multiple = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_tree(self):
        r = [self, []]
        for c in Service.objects.filter(parent_service=self):
            r[1].append(c.get_tree())
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

    def get_workflow(self):
        service_set = self.get_service_set()
        for service in service_set:
            if service.parent_service is None:
                return service.workflow
        return None

    def get_service_set(self):
        service_set = []
        for suborder in self.suborder_set.all():
            service_set.append(suborder.service)
        return service_set

    def __str__(self):
        return self.id.__str__()


class SubOrder(models.Model):
    order = models.ForeignKey('Order')
    service = models.ForeignKey('Service')
    description = models.TextField(default='', blank=True)
    count = models.IntegerField(default=0)


class WorkflowLog(models.Model):
    order = models.ForeignKey('Order')
    step_move = models.ForeignKey('StepMove')
    description = models.TextField('Step')
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # if self.pk is None:
            # sms_client = NetScSmsClient()
            # sms_client.send_sms(['9136496628'], self.step_move.message)
        super(WorkflowLog, self).save(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    address = models.TextField()
    postal_code = models.CharField(max_length=16)
    phone = models.CharField(max_length=16)
    is_confirmed = models.BooleanField(default=False)
    balance = models.IntegerField(default=0)


class StepMove(models.Model):
    title = models.CharField(max_length=256, default='')
    into_step = models.ForeignKey('Step', related_name='from_step_move_set', default=2)
    from_step = models.ForeignKey('Step', related_name='into_step_move_set', default=1)
    message = models.TextField()
    user_groups = models.ManyToManyField('auth.Group')
