from django.conf.urls import include, url
from . import views
from .views import PostDelete
urlpatterns = [
	url(r'^$', views.post_list,name='post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
	url(r'^post/new/$', views.post_new, name='post_new'),
	
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^post/delete/(?P<pk>[0-9]+)$', PostDelete.as_view(), name='post_delete_post'),
	
]