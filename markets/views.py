from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .exceptions import InsufficientFunds
from .models import Coins, Transactions
from .serializers import (
    CoinSerializer,
    CreateTransactionRequestSerializer,
    TransactionSerializer,
)


class CoinView(APIView):

    def get(self, request, symbol: str):
        coin = get_object_or_404(Coins, symbol=symbol)

        serializer = CoinSerializer(coin)
        return Response(serializer.data)


class TransactionsView(APIView):

    def post(self, request, symbol: str):
        req_serializer = CreateTransactionRequestSerializer(data=request.data)
        req_serializer.is_valid(raise_exception=True)
        req_body = req_serializer.validated_data

        coin = get_object_or_404(Coins, symbol=symbol)

        user = request.user
        wallet = user.wallet

        cost = coin.price * req_body.get("amount")
        if cost > wallet.balance:
            raise InsufficientFunds

        trans = Transactions(
            user=request.user,
            coin=coin,
            amount=req_body.get("amount"),
            price=coin.price,
        )
        trans.save()

        wallet.balance -= cost
        wallet.save()

        return Response(TransactionSerializer(trans).data)
