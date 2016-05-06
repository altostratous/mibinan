
from django.conf.urls import url

from . import views
from .controllers import orders

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^orders/add$', orders.orders_add, name='orders_add'),
    url(r'^orders$', orders.index, name='orders'),
    url(r'^orders/edit/(?P<id>[0-9]+)', orders.edit, name='orders_edit'),
    url(r'^orders/forward/(?P<id>[0-9]+)', orders.forward, name='orders_forward'),
    url(r'^orders/backward/(?P<id>[0-9]+)', orders.backward, name='orders_backward')
]
