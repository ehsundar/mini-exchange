from abc import ABC, abstractmethod


class Settler(ABC):
    @abstractmethod
    def settle_transactions(self, coin_symbol: str):
        pass
