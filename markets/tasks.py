import logging

from celery import shared_task

logger = logging.getLogger(__name__)


@shared_task()
def settle_transactions(coin_symbol: str):
    logger.info("Settling transactions for %s", coin_symbol)
