from django.shortcuts import render
from ..forms import *
from django.http import HttpResponse
from ..helpers.service import ServicesHelper
from ..helpers.workflow import WorkflowHelper
from django.contrib.auth.decorators import *


@login_required
def orders_add(request):
    if request.method == 'POST':
        service_ids = dict(request.POST)['service_ids']
        service_counts = dict(request.POST)['service_counts']
        service_descriptions = dict(request.POST)['service_descriptions']
        the_order = Order()
        the_order.user = request.user
        the_order.full_clean()
        the_order.save()
        log = WorkflowLog()
        log.order = the_order
        log.description = "سفارش سبت شد."
        log.step_move = StepMove.objects.get(into_step=Step.objects.get(order=1), from_step=Step.objects.get(order=2))
        log.save()
        for i in range(service_ids.__len__()):
            if ("service_checkboxes_%s" % service_ids[i]) in dict(request.POST):
                sub_order = SubOrder()
                sub_order.service = Service.objects.get(id=service_ids[i])
                sub_order.order = the_order
                sub_order.description = service_descriptions[i]
                sub_order.count = service_counts[i]
                sub_order.full_clean()
                sub_order.save()
        return render(request, "main/successful.html", {'title_for_layout': 'فرایند موفق',
                                                        'transaction_name': 'ثبت سفارش'})
    else:
        parent_service = Service.objects.get(id=1)
        return render(request, 'main/orders/add.html', {'title_for_layout': 'ثبت سفارش',
                                                   'services': ServicesHelper(parent_service.get_tree())})


@login_required
def index(request):
    data = Order.objects.filter(user=request.user)
    return render(request, 'main/orders/index.html', {'orders': data})


def edit(request, id):
    data = Order.objects.get(user=request.user, id=id)
    return render(request, 'main/orders/edit.html', {'order': data,
                                                     'workflow': WorkflowHelper(data)})


def forward(request, id):
    # do stuff
    return edit(request, id)


def backward(request, id):
    # do stuff
    return edit(request, id)
