from django.conf.urls import patterns, include, url
from django.contrib import admin

from calvin.apps.temperature.views import yo_view

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'calvin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^yo/', yo_view, name='yo'),

    # TODO: Need media for latest image
)
