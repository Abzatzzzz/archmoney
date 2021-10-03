from .models import DepCategory, WithCategory


class DepCategoryModelRepository:
    def __init__(self, request):
        self._request = request

    def get_user_depcategories(self):
        user = self._request.user
        empty_queryset = DepCategory.objects.none()
        return (
            DepCategory.objects.filter(user=user)
            if user.is_authenticated
            else empty_queryset
        )


class WithCategoryModelRepository:
    def __init__(self, request):
        self._request = request

    def get_user_withcategories(self):
        user = self._request.user
        empty_queryset = WithCategory.objects.none()
        return (
            WithCategory.objects.filter(user=user)
            if user.is_authenticated
            else empty_queryset
        )
