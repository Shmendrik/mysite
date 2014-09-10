from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'^$', views.main, name='main'),
	url(r'^(?P<post_id>\d+)/$', views.detail, name='detail'),
	url(r'^(?P<post_id>\d+)/add_comment/$', views.add_comment, name='add_comment'),	
)
