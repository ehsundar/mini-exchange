import logging

from celery import shared_task

from markets.foreign_exchange import BinanceExchangeStub

from .settlers import BatchCoinSettler

logger = logging.getLogger(__name__)

# TODO: Use dependency injection.
exchange_stub = BinanceExchangeStub()


@shared_task()
def settle_transactions(coin_symbol: str):
    logger.info("Settling transactions for %s", coin_symbol)

    settler = BatchCoinSettler(exchange_stub, 10.0)
    settler.settle_transactions(coin_symbol)
