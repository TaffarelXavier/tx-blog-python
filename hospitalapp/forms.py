from django import forms
from .models import Hospital


class Hospitalform(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'
        # widgets = {
        #     'desc_hospital': forms.TextField(attrs={'class': 'myfieldclass'}),
        # }
