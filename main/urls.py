
from django.conf.urls import url

from . import views
from .controllers import orders

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^orders/add$', orders.orders_add, name='orders_add'),
    url(r'^orders$', orders.index, name='orders'),
    url(r'^orders/edit/(?P<id>[0-9]+)', orders.edit, name='orders_edit')
]
