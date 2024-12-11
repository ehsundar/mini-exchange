from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .exceptions import InsufficientFunds
from .models import Coins, Transactions
from .serializers import CoinSerializer


class CoinView(APIView):

    def get(self, request, symbol: str):
        coin = get_object_or_404(Coins, symbol=symbol)

        serializer = CoinSerializer(coin)
        return Response(serializer.data)

    def post(self, request, symbol: str):
        coin = get_object_or_404(Coins, symbol=symbol)

        user = request.user
        wallet = user.wallet

        cost = coin.price * request.data["amount"]
        if cost > wallet.balance:
            raise InsufficientFunds

        trans = Transactions(
            user=request.user,
            coin=coin,
            amount=request.data["amount"],
            price=coin.price,
        )
        trans.save()
