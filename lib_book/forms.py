from django import forms


class ReaderForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    patronymic = forms.CharField(max_length=100, required=False)
