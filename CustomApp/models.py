"""Model definition for workflow operations"""

from django.contrib.auth.models import User, Group
from django.db.models import (
    Model,
    DateTimeField,
    BooleanField)
from helpers import get_request_params, flow_config


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
    def title(self):
        """Returns entity title"""
        return self.__class__.__name__

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
    is_active = BooleanField('Is Active', default=True)
    process_status = CharField(choices=TASK_STATUS, max_length=20)
    request_status = CharField(choices=REQUEST_STATUS, max_length=20)


def get_app_detail(request, **kwargs):
    app_title = get_request_params('app_name', request, **kwargs)
    config = flow_config(app_title)
    return config
