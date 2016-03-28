
from django.conf.urls import include , url
from django.contrib import admin
from blog.views import post_detail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
]
