from abc import ABC, abstractmethod


class GlobalMarketStub(ABC):

    @abstractmethod
    def buy(self, amount: float, coin_symbol: str):
        pass


class BinanceStub(GlobalMarketStub):
    def __init__(self, http_client):
        self.http_client = http_client

    def buy(self, amount: float, coin: str):
        pass
