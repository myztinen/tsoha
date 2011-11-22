from django import forms

class SearchForm(forms.Form):
    search_parameter = forms.CharField(max_length=30)
    search_target = forms.CharField()
    
class AddRecipeForm(forms.Form):
    drink_name = forms.CharField(max_length=30)
    drink_type = forms.CharField(max_length=30)
    first_ingredient = forms.CharField(max_length=30)
    first_amount = forms.CharField(max_length=30)
    second_ingredient = forms.CharField(max_length=30)
    second_amount = forms.CharField(max_length=30)
    third_ingredient = forms.CharField(max_length=30)
    third_amount = forms.CharField(max_length=30)
    fourth_ingredient = forms.CharField(max_length=30)
    fourth_amount = forms.CharField(max_length=30)

