from django import forms
from .models import DepCategory, WithCategory, Deposit


class DepCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = DepCategory
        fields = ["title"]


class WithCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = WithCategory
        fields = ["title"]


class DepositCreateForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = ["uan", "category", "title"]


class WithdrawForm(forms.Form):
    uan = forms.DecimalField(label="UAN", required=True)
    categories = forms.ModelMultipleChoiceField(queryset=WithCategory.objects.all())
    title = forms.CharField(required=False, max_length=50)


#class DateForm(forms.Form):
#    OPTIONS = (("day": "today"),("week": "week"), ("month": "month"), 
#            ("year": "year"), ("all_time": "archive/"),
#            )
#    time_period = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS)
