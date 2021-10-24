from django import forms
from .models import DepCategory, WithCategory, Deposit, Withdraw



class DepCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = DepCategory
        fields = ["title"]


class WithCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = WithCategory
        fields = ["title"]


class DepositCreateForm(forms.ModelForm):

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs) # Расширение базового класса
        self.fields["category"].queryset = DepCategory.objects.filter(user=user)


    class Meta:
        model = Deposit
        fields = ["uan", "category", "title"]


class WithdrawCreateForm(forms.ModelForm):

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs) # Расширение базового класса
        self.fields["category"].queryset = WithCategory.objects.filter(user=user)


    class Meta:
        model = Withdraw
        fields = ["uan", "category", "title"]

