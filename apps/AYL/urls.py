from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^content/(?P<id>\d+)$', views.content),
    url(r'^login_registration$', views.loginpage),
    url(r'^login$', views.login),
    url(r'^register$', views.register),

]
