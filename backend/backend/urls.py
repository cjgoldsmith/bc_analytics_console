from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

urlpatterns = patterns('',
    # Examples:
    url(r'^', include('bc_analytics.urls')),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
