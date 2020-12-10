from django import forms
from .models import Hospital, Post


class Hospitalform(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'
        # widgets = {
        #     'desc_hospital': forms.TextField(attrs={'class': 'myfieldclass'}),
        # }
        
class PostsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        # widgets = {
        #     'desc_hospital': forms.TextField(attrs={'class': 'myfieldclass'}),
        # }
