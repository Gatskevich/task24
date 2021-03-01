from django import forms


class StorageForm(forms.Form):
    name = forms.CharField(label='name0')