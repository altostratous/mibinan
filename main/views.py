from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
# Create your views here.

from django.http import HttpResponse


# @permission_required('add_user')
def index(request):
    return render(request, 'main/index.html', {})
