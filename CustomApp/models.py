import sys
from django.contrib.auth.models import User, Group
from django.db.models import (
    Model,
    DateTimeField,
    BooleanField,
    CharField,
    ForeignKey,
    IntegerField)
from helpers import get_request_params, flow_config
from constants import TASK_STATUS, PROCESS_STATUS, REQUEST_STATUS


class AbstractEntity(Model):
    """Common attributes for all models"""
    creation_date = DateTimeField('Creation Date', auto_now_add=True)
    last_updated = DateTimeField('Last Updated', auto_now=True)

    class Meta(object):
        abstract = True

    @property
    def class_meta(self):
        """Returns class meta"""
        return self._meta

    @property
    def module_label(self):
        """Returns module label"""
        return self.class_meta.app_label

    @property
    def code(self):
        """Returns a unique code"""
        return "{0}-{1}-{2}".format(
            self.class_meta.app_label,
            self.title,
            self.id)

    def __unicode__(self):
        """Returns ID"""
        return str(self.id)


class AbstractProcess(AbstractEntity):
    user = ForeignKey(User, related_name='requester')
    is_active = BooleanField('Is Active', default=True)
    process_status = CharField(choices=TASK_STATUS, max_length=20, default="In Progress")
    request_status = CharField(choices=REQUEST_STATUS, max_length=20, default="Initiated")

    class Meta:
        abstract = True


class AbstractTransaction(AbstractEntity):
    role = CharField(verbose_name="role", max_length=30)
    class Meta:
        abstract = True


def get_app_detail(request, **kwargs):
    app_title = get_request_params('app_name', request, **kwargs)
    config = flow_config(app_title)
    return config


def get_queryset(request, **kwargs):
    config = get_app_detail(request, **kwargs)
    queryset = can_approve(request, config)
    return queryset


def can_approve(request, config):
    model = config.PROCESS[config.INITIAL]['model']
    transition = config.PROCESS[config.INITIAL]['transitions']
    queryset = model.objects.filter(id=0)
    for i in range(20):
        if not transition:
            break
        transition = transition[0]
        method = config.PROCESS[transition]['method']
        role = config.PROCESS[transition]['role']
        access = method(request, role)
        if access:
            queryset = queryset | access
        transition = config.PROCESS[transition]['transitions']
    return queryset

