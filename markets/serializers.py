from rest_framework import serializers

from .models import Coins, Transactions


class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coins
        fields = (
            "symbol",
            "name",
            "price",
            "created_at",
            "updated_at",
        )


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = (
            "id",
            "user",
            "coin",
            "amount",
            "price",
            "created_at",
            "updated_at",
        )


class CreateTransactionRequestSerializer(serializers.Serializer):
    amount = serializers.FloatField()
