from __future__ import unicode_literals
from django.conf.urls import url

from django.db import models

# Create your models here.
urlpatterns = [
    url(r'^$', taskprocess, name='taskprocess')
]