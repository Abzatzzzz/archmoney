from .models import DepCategory, WithCategory, Deposit


class AllDepModelRepository:
    def __init__(self, request):
        self._request = request

    def get_user_all_deposits(self):
        user = self._request.user
        empty_queryset = Deposit.objects.none()
        return Deposit.objects.filter(user=user) if user.is_authenticated else empty_queryset



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
