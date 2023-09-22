from django import forms
from .models import Post

class Form(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 5,
            'style': 'width: 100%'
        })
    )
    class Meta:
        model = Post
        fields = '__all__'
