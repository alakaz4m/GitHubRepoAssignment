from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'new$', views.addUser),
    url(r'create$', views.process),
    url(r'(?P<user_id>\d+)$', views.show),
    url(r'(?P<user_id>\d+)/edit$', views.edit),
    url(r'(?P<user_id>\d+)/delete$', views.destroy),
]
