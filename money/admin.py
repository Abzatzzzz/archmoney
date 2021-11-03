from django.contrib import admin

from .models import *


class DepositAdmin(admin.ModelAdmin):
    list_display = ('date', 'user', 'category', 'uan')
    list_display_links = ('date', 'user', 'category')
    search_fields = ('date', 'title')


class WithdrawAdmin(admin.ModelAdmin):
    list_display = ('date', 'user', 'category', 'uan')
    list_display_links = ('date', 'user', 'category')
    search_fields = ('date', 'title')


admin.site.register(Deposit, DepositAdmin)
admin.site.register(Withdraw, WithdrawAdmin)
admin.site.register(WithCategory)
admin.site.register(DepCategory)
