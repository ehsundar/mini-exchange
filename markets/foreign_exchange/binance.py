import logging
import uuid

from .base import ExchangeStub

logger = logging.getLogger(__name__)


class BinanceExchangeStub(ExchangeStub):
    def buy(self, currency_symbol: str, amount: float) -> str:
        logger.info("Buying %f %s", amount, currency_symbol)
        return str(uuid.uuid4())

    def min_buy_amount_dollars(self, currency_symbol: str) -> float:
        return 8.0
