from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Balance, Transaction


class UserSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source="id", read_only=True)
    class Meta:
        model = User
        fields = ['user_id', 'username', 'email']


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    transaction_id = serializers.PrimaryKeyRelatedField(source="id", read_only=True)
    username = serializers.CharField(source="user.username", read_only=True)
    user_id = serializers.IntegerField(source="user.id")
    class Meta:
        model = Transaction
        fields = ['transaction_id', 'user_id', 'username', 'date', 'value']


class BalanceSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    user_id = serializers.IntegerField(source="user.id")
    class Meta:
        model = Balance
        fields = ['username', 'user_id', 'score']
