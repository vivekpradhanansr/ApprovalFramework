from rest_framework import serializers
from models import Reimburse, Transaction


class ReimburseSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100, default='')
    reason = serializers.CharField(max_length=100, default='')
    amount = serializers.IntegerField()
    class Meta:
        model = Reimburse
        fields = ( 'title', 'reason', 'amount')

    def save(self):
        title = self.validated_data['title']
        reason = self.validated_data['reason']
        amount = self.validated_data['amount']
        Reimburse(title=title,
                  reason=reason,
                  amount=amount,
                  user=user_id,
                  process_status="Initiated",
                  request_status="In Progress").save()



class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('reimburse', 'approved_by', 'status')