from typing import Any, Dict

from django.http import HttpRequest
from . import models


class DepositModelService:
    def __init__(self, request):
        self._request = request

    def create(self, data):
        models.Deposit.objects.create(
            user=self._request.user,
            title=data["title"],
            uan=data["uan"],
            category=data["category"],
        )


class WithdrawModelService:
    def __init__(self, request):
        self._request = request

    def create(self, data):
        models.Withdraw.objects.create(
            user=self._request.user,
            title=data["title"],
            uan=data["uan"],
            category=data["category"],
        )


class DepCategoryModelService:
    def __init__(self, request: HttpRequest) -> None:
        self._request = request

    def create(self, data: Dict[str, Any]) -> None:
        models.DepCategory.objects.create(user=self._request.user, title=data["title"])


class WithCategoryModelService:
    def __init__(self, request: HttpRequest) -> None:
        self._request = request

    def create(self, data: Dict[str, Any]) -> None:
        models.WithCategory.objects.create(user=self._request.user, title=data["title"])
