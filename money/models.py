from django.db import models


class Deposit(models.Model):
    title = models.CharField(max_length=50, blank=True)
    category = models.CharField(max_length=50)
    uan = models.DecimalField(max_digits=7, decimal_places=2)
    usd = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.category


class Withdraw(models.Model):
    title = models.CharField(max_length=50, blank=True)
    category = models.CharField(max_length=50)
    uan = models.DecimalField(max_digits=7, decimal_places=2)
    usd = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.category

