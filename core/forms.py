from django import forms
from .models import list


class ListForm(forms.ModelForm):
    class Meta:
        model = list
        widgets={
            'item': forms.TextInput(attrs={'class': 'form-control'}),
            'completed': forms.EmailInput(attrs={'class': 'form-control'}),
        }
        fields = ["item", "completed"]
