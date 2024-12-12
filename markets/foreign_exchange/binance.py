import logging
import uuid

from .base import ExchangeStub

logger = logging.getLogger(__name__)


class BinanceExchangeStub(ExchangeStub):
    def buy(self, amount: float, coin: str) -> str:
        logger.info("Buying %f %s", amount, coin)
        return str(uuid.uuid4())

    def min_buy_amount_dollars(self, coin: str) -> float:
        return 8.0
