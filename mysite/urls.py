
from django.conf.urls import include , url
from django.contrib import admin
import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
	url(r'^', include('users.urls', namespace='users')),

    #Python Social Auth
	url('', include('social.apps.django_app.urls', namespace='social')),
]
