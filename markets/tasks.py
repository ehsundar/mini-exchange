import logging

from celery import shared_task

from markets.foreign_exchange import BinanceExchangeStub

from .settlers import BatchCoinSettler

logger = logging.getLogger(__name__)

# TODO: Use dependency injection. pylint: disable=fixme
exchange_stub = BinanceExchangeStub()


@shared_task()
def settle_transactions(coin_symbol: str):
    """
    Settle transactions with foreign exchange for a given coin.
    :param coin_symbol: coin symbol to settle transactions for.
    :return: None
    """
    logger.info("Settling transactions for %s", coin_symbol)

    settler = BatchCoinSettler(exchange_stub, 10.0)
    settler.settle_transactions(coin_symbol)
