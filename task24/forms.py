from django import forms


class StorageForm(forms.Form):
    name0 = forms.CharField(label='name0')