from rest_framework import serializers


class TransactionsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    process = serializers.CharField()
    status = serializers.ChoiceField()
    approved_by = serializers.CharField()

    def create(self, validated_data):
        return True

    def update(self, instance, validated_data):
        return True
