from django import forms

class SearchForm(forms.Form):
    parameter = forms.CharField(max_length=30)
    target = forms.CharField()

