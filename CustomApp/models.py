from __future__ import unicode_literals

from django.db.models import (
    Model,
    DateTimeField)


class ProcessEntity(Model):
    creation_date = DateTimeField('Creation Date', auto_now_add=True)
    last_updated = DateTimeField('Last Updated', auto_now=True)

    class Meta(object):
        abstract = True

    @property
    def class_meta(self):
        return self._meta

    @property
    def title(self):
        return self.__class__.__name__

    @property
    def module_label(self):
        return self.class_meta.app_label

    @property
    def code(self):
        return "{0}-{1}-{2}".format(
            self.class_meta.app_label,
            self.title,
            self.id
        )
