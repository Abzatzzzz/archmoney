from django import forms
from django.core.exceptions import ValidationError
from .models import DepCategory, WithCategory
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="User name")
    password = forms.CharField(
        label="Password")


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label="User name",
        help_text="Choose your Name",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class DepositForm(forms.Form):
    uan = forms.DecimalField(label="UAN", required=True)
    categories = forms.ModelMultipleChoiceField(queryset=DepCategory.objects.all())
    title = forms.CharField(required=False, max_length=50)


class WithdrawForm(forms.Form):
    uan = forms.DecimalField(label="UAN", required=True)
    categories = forms.ModelMultipleChoiceField(queryset=WithCategory.objects.all())
    title = forms.CharField(required=False, max_length=50)
