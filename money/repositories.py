from .models import DepCategory


class DepCategoryModelRepository:
    def __init__(self, request):
        self._request = request

    
    def get_user_depcategories(self):
        user = self._request.user
        empty_queryset = DepCategory.objects.none()
        return DepCategory.objects.filter(user=user) if user.is_authenticated else empty_queryset

