from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^angular_dashboard/', include('angular_dashboard.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
