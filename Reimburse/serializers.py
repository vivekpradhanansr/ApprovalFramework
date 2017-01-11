from rest_framework import serializers
from models import Reimburse, Transaction


class ReimburseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reimburse
        fields = ('id', 'title', 'user', 'reason', 'process_status', 'request_status', 'amount')


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('reimburse', 'approved_by', 'status')