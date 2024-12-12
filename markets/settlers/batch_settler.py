import logging

from django.db import transaction
from django.db.models import Sum

from markets.foreign_exchange import ExchangeStub

from ..models import Coins, Settlements, Transactions
from .base import Settler

logger = logging.getLogger(__name__)


class BatchCoinSettler(Settler):
    def __init__(self, exchange_stub: ExchangeStub, buy_lower_limit: float):
        self._exchange_stub = exchange_stub
        self._buy_lower_limit = buy_lower_limit

    def settle_transactions(self, coin_symbol: str):
        logger.info("Settling transactions for %s", coin_symbol)

        coin = Coins.objects.get(symbol=coin_symbol)

        with transaction.atomic():
            trx_set = Transactions.objects.filter(
                coin__symbol=coin_symbol, settlement__isnull=True
            )

            total_amount = (
                trx_set.aggregate(total_amount=Sum("amount")).get("total_amount") or 0
            )

            if total_amount < 0.0001:
                logger.warning("No transactions to settle for %s", coin_symbol)
                return

            if total_amount < self._buy_lower_limit:
                logger.info("Insufficient total amount for %s to settle", coin_symbol)
                return

            exchange_buy_lower_limit = (
                self._exchange_stub.min_buy_amount_dollars(coin.symbol) / coin.price
            )

            if total_amount < exchange_buy_lower_limit:
                logger.warning(
                    "exchange limit is lower than our limit %d on %s",
                    exchange_buy_lower_limit,
                    coin_symbol,
                )
                return

            external_id = self._exchange_stub.buy(total_amount, coin.symbol)

            settlement = Settlements.objects.create(
                coin=coin, amount=total_amount, external_id=external_id
            )

            trx_set.update(settlement=settlement)
