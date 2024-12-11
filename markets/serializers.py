from rest_framework import serializers

from .models import Coins


class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coins
        fields = "__all__"
