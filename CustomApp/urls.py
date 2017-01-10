from __future__ import unicode_literals
from django.conf.urls import url
from views import ProcessStart, process, ProcessListView
from django.db import models

# Create your models here.
urlpatterns = [
    url(r'^$', process, name='taskprocess'),
    url(
        r'^(?P<app_name>\w+)$',
        ProcessListView.as_view(),
        name="create"
    )

]