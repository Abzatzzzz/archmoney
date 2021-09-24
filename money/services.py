from typing import Any

from django.http import HttpRequest
from . import models


class DepCategoryModelService:
    def __init__(self, request: HttpRequest) -> None:
        self._request = request


    def create(self, data: dict[str, Any]) -> None:
        models.DepCategory.objects.create(
            user=self._request.user, title=data["title"]
        )
