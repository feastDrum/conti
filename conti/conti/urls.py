from django.conf.urls import include, url
from django.contrib import admin
from django.views import defaults
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('contiSvc.urls')),
]
