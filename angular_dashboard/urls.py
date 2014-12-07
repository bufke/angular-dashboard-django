from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from . import views


urlpatterns = patterns('',
    url(r'^demo/', TemplateView.as_view(template_name="angular_dashboard/dashboard.html")),
    url(r'^api/(?P<key>\w+)', login_required(views.StorageView.as_view())),
)
