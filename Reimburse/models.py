from CustomApp.models import ProcessEntity
from django.contrib.auth.models import User
from django.db.models import (
    CharField,
    ForeignKey,
    IntegerField,
    BooleanField,
    TextField
)
from CustomApp.constants import TASK_STATUS, REQUEST_STATUS, PROCESS_STATUS


class Reimburse(ProcessEntity):
    user = ForeignKey(User)
    is_active = BooleanField()
    title = CharField(max_length=50)
    reason = TextField(null=True, blank=True)
    process_status = CharField(choices=TASK_STATUS, max_length=20)
    request_status = CharField(choices=REQUEST_STATUS, max_length=20)
    amount = IntegerField()

    def __unicode__(self):
        return self.user.first_name


class Transaction(ProcessEntity):
    reimburse = ForeignKey(Reimburse)
    approved_by = ForeignKey(User)
    status = CharField(choices=PROCESS_STATUS, max_length=20)




