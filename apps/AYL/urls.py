from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^login_registration$', views.loginpage),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^addcontentpage$', views.addcontentpage),
    url(r'^addcontent$', views.addcontent),
    url(r'^content$', views.content),
    url(r'^content/(?P<content_id>\d+)?$', views.content),
    url(r'^like/(?P<content_id>\d+)?$', views.like),
    url(r'^logout$', views.logout)
    url(r'^comments/(?P<content_id>\d+)?$', views.add_comments

]

if settings.DEBUG is True:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
