"""anything_you_like URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from apps.AYL.models import User, Content, Comment, Like
class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)
class ContentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Content, ContentAdmin)
class CommentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Comment, CommentAdmin)
class LikeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Like, LikeAdmin)

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^', include('apps.AYL.urls')),
]
