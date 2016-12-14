from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.place_order),
    url(r'pizza/(?P<order_id>\d+)$', views.order_pizza),
    url(r'bread/(?P<order_id>\d+)$', views.order_bread),
]

