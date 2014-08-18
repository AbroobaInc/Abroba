'''
Created on Aug 18, 2014

@author: Fabio Ayres
'''
from django.conf.urls import patterns, include, url
from Cocrete import views


urlpatterns = patterns('',
    # Examples: abrooba!
    # url(r'^$', 'Abroba.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
)