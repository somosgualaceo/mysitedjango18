from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    #url(r'^log-out/$', 'apps.users.views.LogOut', name='logout'),
    #url(r'^extra-data/$', ExtraDataView.as_view(), name='extra_data'),
    url(r'^log-out/$', 'users.views.LogOut', name='logout'),
)