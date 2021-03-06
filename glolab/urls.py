"""glolab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url,patterns
from django.contrib import admin
from django.views.generic import TemplateView
from userpro import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^student/$',views.allstudents, name='register'),
    url(r'^student/register/$',views.register, name='register'),
    url(r'^student/editprofile/$', views.editstudentprofile, name='editstudentprofile'),
    url(r'^student/edit/$',views.editprofile,name='edit'),
    url(r'^company/register/$',views.companyregister,name='companyregister'),
    url(r'^company/edit/$',views.editcompanyprofile,name='companyedit'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^projects/', include('projects.urls')),
    (r'^accounts/',include('registration.backends.simple.urls')),
    
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# UNDERNEATH your urlpatterns definition, add the following two lines:
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )