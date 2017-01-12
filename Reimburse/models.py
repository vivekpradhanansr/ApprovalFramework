from CustomApp.models import AbstractEntity
from django.contrib.auth.models import User
from django.db.models import (
    Model,
    CharField,
    ForeignKey,
    IntegerField,
    BooleanField,
    TextField
)
from CustomApp.constants import TASK_STATUS, REQUEST_STATUS, PROCESS_STATUS


class Reimburse(AbstractEntity):
    user = ForeignKey(User)
    title = CharField(max_length=50)
    reason = TextField(null=True, blank=True)

    amount = IntegerField()

    def clean(self):
        """Custom validation logic should go here"""
        pass


class Transaction(AbstractEntity):
    reimburse = ForeignKey(Reimburse)
    approved_by = ForeignKey(User)
    status = CharField(choices=PROCESS_STATUS, max_length=20)




