from __future__ import unicode_literals
from django.conf.urls import url
from views import taskprocess
from django.db import models

# Create your models here.
urlpatterns = [
    url(r'^$', taskprocess, name='taskprocess'),
    url(
        r'^(?P<app_name>\w+)$',
        WorkflowDetail.as_view(),

    )
]