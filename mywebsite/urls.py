from django.urls import re_path as url, include
from django.contrib import admin
from mywebsite import views

urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^project/', include('project.urls')),
]
