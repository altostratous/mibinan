from django.shortcuts import render
from .forms import *
from django.http import HttpResponse
from .helpers.service import ServicesHelper

# from django.contrib.auth.decorators import permission_required
# Create your views here.


# @permission_required('add_user')
def index(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        return HttpResponse(form)
    else:
        form = ServiceForm()
        return render(request, 'main/simpleform.html', {'title_for_layout': 'hello',
                                                        'form': form,
                                                        'nav_bar': {'اول': 'hello', 'دوم': 'hello'}})


def order(request):
    if request.method == 'POST':
        pass
    else:
        parent_service = Service.objects.get(id=1)
        # return HttpResponse(parent_service.title)
        return render(request, 'main/order.html', {'title_for_layout': 'ثبت سفارش',
                                                   'services': ServicesHelper(parent_service.get_tree())})
