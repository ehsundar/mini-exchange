import uuid

from .base import ExchangeStub


class BinanceExchangeStub(ExchangeStub):
    def __init__(self, http_client):
        self.http_client = http_client

    def buy(self, amount: float, coin: str) -> str:
        return str(uuid.uuid4())
