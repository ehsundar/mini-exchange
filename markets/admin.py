from django.contrib import admin

from .models import Coins, Transactions, Wallets

admin.site.register(Coins)
admin.site.register(Wallets)
admin.site.register(Transactions)
