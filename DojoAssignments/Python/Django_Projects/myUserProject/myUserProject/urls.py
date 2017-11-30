from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^users/', include('apps.userApp.urls')),
    url(r'^admin/', admin.site.urls),
]
