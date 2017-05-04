from django.conf.urls import url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
<<<<<<< HEAD
    url(r'^addcontentpage$', views.addcontentpage),
    url(r'^addcontent$', views.addcontent)
=======
    url(r'^content/(?P<id>\d+)$', views.content),
    url(r'^login_registration$', views.loginpage),
    url(r'^login$', views.login),
    url(r'^register$', views.register),

>>>>>>> b06db6dc1177b26b65136e0eec03a358ac3e4fb9
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
