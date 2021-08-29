from django.contrib import admin

from .models import *


admin.site.register(Deposit)
admin.site.register(Withdraw)
admin.site.register(WithCategory)
admin.site.register(DepCategory)
