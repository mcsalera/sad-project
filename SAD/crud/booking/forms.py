from django import forms

class SearchForm(forms.Form):
    location = forms.CharField(label='', max_length=100)
    max_price = forms.IntegerField(label='')

    location.widget.attrs.update({'class': 'form-control', 'placeholder': 'Location'})
    max_price.widget.attrs.update({'class': 'form-control', 'placeholder': 'Max price to be charged'})