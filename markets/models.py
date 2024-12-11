import uuid

from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Coins(models.Model):
    symbol = models.CharField(
        primary_key=True,
        max_length=10,
        validators=[
            RegexValidator(r"^[A-Z]{2,10}$", message="Invalid symbol"),
        ],
    )

    name = models.CharField(max_length=100)
    price = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.symbol})"


class Wallets(models.Model):
    owner = models.OneToOneField(
        "auth.User",
        on_delete=models.PROTECT,
        primary_key=True,
        editable=False,
        related_name="wallet",
    )

    balance = models.FloatField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.owner.username} - {self.balance}"


class Transactions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey("auth.User", on_delete=models.PROTECT)

    coin = models.ForeignKey(Coins, on_delete=models.PROTECT)
    amount = models.FloatField()
    price = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.coin.symbol} - {self.amount}"


@receiver(post_save, sender="auth.User")
def create_user_wallet(instance, created, **__):
    if created:
        Wallets.objects.create(owner=instance)
