from django.conf.urls import url
from . import views

app_name = 'service'

urlpatterns = [
    url(r'^$', views.service_list, name='service_list'),
    url(r'^(?P<service_id>[0-9]+)/$', views.detail, name='detail'),
]
