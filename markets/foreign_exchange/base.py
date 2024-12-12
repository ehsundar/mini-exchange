from abc import ABC, abstractmethod


class ExchangeStub(ABC):
    @abstractmethod
    def buy(self, currency_symbol: str, amount: float) -> str:
        """
        Buy an amount of currency.
        :param currency_symbol: BTC, ETH, etc.
        :param amount: amount to buy.
        :return: foreign exchange transaction ID.
        """
        pass
