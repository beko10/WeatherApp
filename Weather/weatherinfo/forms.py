from django import forms


class WeatherForm(forms.Form):
    sehir = forms.CharField(max_length=100)