from rest_framework import serializers
from constants import REQUEST_STATUS, TASK_STATUS

class TransactionsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    process = serializers.ChoiceField(TASK_STATUS)
    status = serializers.ChoiceField(REQUEST_STATUS)
    approved_by = serializers.CharField()

    def create(self, validated_data):
        return True

    def update(self, instance, validated_data):
        return True
