
from django import forms

class SearchForm(forms.Form):
    country = forms.CharField(label='', max_length=100)
    city = forms.CharField(label='', max_length=100,required=False)
    price = forms.IntegerField(label='')

    country.widget.attrs.update({'class': 'form-control', 'placeholder': 'Country'})
    city.widget.attrs.update({'class': 'form-control', 'placeholder': 'City'})
    price.widget.attrs.update({'class': 'form-control', 'placeholder': 'Max price to be charged'})