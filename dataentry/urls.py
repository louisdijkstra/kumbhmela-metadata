from django.conf.urls import url

from . import views 

__author__ = "Louis Dijkstra"



# list of url patterns
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<model_str>[\w-]+)/list$', views.view_list, name='list'),
	url(r'^(?P<model_str>[\w-]+)/(?P<object_id>[0-9]+)$', views.view_detail, name='detail'),
	url(r'^files/(?P<model_str>[\w-]+)(?P<object_id>[0-9]+)/$', views.view_subset_files, name='list'),
]