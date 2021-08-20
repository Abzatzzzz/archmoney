from django import forms
from django.core.exceptions import ValidationError
from .models import DepCategory, WithCategory


class DepositForm(forms.Form):
    uan = forms.DecimalField(label="UAN", required=True)
    categories = forms.ModelMultipleChoiceField(queryset=DepCategory.objects.all())
    title = forms.CharField(required=False, max_length=50)


class WithdrawForm(forms.Form):
    uan = forms.DecimalField(label="UAN", required=True)
    categories = forms.ModelMultipleChoiceField(queryset=WithCategory.objects.all())
    title = forms.CharField(required=False, max_length=50)
