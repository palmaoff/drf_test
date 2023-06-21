from api.models import Balance
from .models import Transaction
from django.db.models import Sum


def update_balance(user):
    balance = Balance.objects.filter(user=user).first()

    if balance == None:
        balance = Balance.objects.create(score=0, user=user)

    score = Transaction.objects.filter(user=user).aggregate(Sum('value'))
    balance.score = score['value__sum']
    balance.save()
