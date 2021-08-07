from django.shortcuts import render
from .models import *
from django.db.models import Sum

from datetime import date


def index(request):
    t = str(date.today())
    year = int(t[0:4])
    month = int(t[5:7])
    all_deposits = Deposit.objects.filter(date__month=month)
    all_withdraws = Withdraw.objects.filter(date__month=month)
    p = Deposit.objects.aggregate(Sum("uan"))
    positive_balance = p["uan__sum"]
    n = Withdraw.objects.aggregate(Sum("uan"))
    negative_balance = n["uan__sum"]
    total_balance = positive_balance - negative_balance
    balances = {
        "positive_balance": positive_balance,
        "negative_balance": negative_balance,
        "total_balance": total_balance,
    }
    context = {
        "all_deposits": all_deposits,
        "all_withdraws": all_withdraws,
        "balances": balances,
    }
    return render(request, "money/index.html", context)


def deposit(request):
    return render(request, 'money/deposit.html')

def withdraw(request):
    return render(request, 'money/withdraw.html')
