from django import forms

class SearchForm(forms.Form):
    search_parameter = forms.CharField(max_length=30)
    search_target = forms.CharField()

