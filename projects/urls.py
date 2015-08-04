from django.conf.urls import patterns, url
from projects import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^add_category/$', views.add_category, name='add_category'),
    	url(r'^(?P<category_name_slug>[\w\-]+)/add_project/$', views.add_project, name='add_project'),
    	url(r'^(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
   		url(r'^(?P<category_name_slug>[\w\-]+)/(?P<project_name_slug>[\w\-]+)$', views.project, name='project'),
        )