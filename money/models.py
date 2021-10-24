from django.contrib.auth.models import User
from django.db import models


class Deposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    category = models.ForeignKey("DepCategory", on_delete=models.DO_NOTHING)
    uan = models.DecimalField(max_digits=7, decimal_places=2)
    usd = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.category.title

    class Meta:
        ordering = ['-id']


class Withdraw(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    category = models.ForeignKey("WithCategory", on_delete=models.DO_NOTHING)
    uan = models.DecimalField(max_digits=7, decimal_places=2)
    usd = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.category.title


class DepCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class WithCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
