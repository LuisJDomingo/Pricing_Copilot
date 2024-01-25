# forms.py
from django import forms

class ImportarCSVForm(forms.Form):
    archivo_csv = forms.FileField()
