from __future__ import unicode_literals
from django.conf.urls import url
from views import StartProcess, process, ProcessListView, ProcessUpdate
from django.db import models

# Create your models here.
urlpatterns = [
    url(r'^$', process, name='taskprocess'),
    url(
        r'^(?P<app_name>\w+)$',
        ProcessListView.as_view(),
        name="list_process"
    ),
    url(
        r'^(?P<app_name>\w+)/create/$',
        StartProcess.as_view(),
        name="create"
    ),
    url(
        r'^(?P<app_name>\w+)/update/(?P<pk>\d+|None)/$',
        ProcessUpdate.as_view(),
        name="update"
    )

]