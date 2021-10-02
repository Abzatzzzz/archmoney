from typing import Any, Dict

from django.http import HttpRequest
from . import models


class DepCategoryModelService:
    def __init__(self, request: HttpRequest) -> None:
        self._request = request


    def create(self, data: Dict[str, Any]) -> None:
        models.DepCategory.objects.create(
            user=self._request.user, title=data["title"]
        )


class WithCategoryModelService:
    def __init__(self, request: HttpRequest) -> None:
        self._request = request


    def create(self, data: Dict[str, Any]) -> None:
        models.WithCategory.objects.create(
            user=self._request.user, title=data["title"]
        )
