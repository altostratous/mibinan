from django.shortcuts import render
from .forms import *
from django.http import HttpResponse

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
