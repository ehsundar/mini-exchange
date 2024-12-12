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

    @abstractmethod
    def min_buy_amount_dollars(self, currency_symbol: str) -> float:
        """
        Get the minimum amount of dollars required to buy a currency.
        :param currency_symbol: BTC, ETH, etc.
        :return: minimum amount of dollars.
        """
