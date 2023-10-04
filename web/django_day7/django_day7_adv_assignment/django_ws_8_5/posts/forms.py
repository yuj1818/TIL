from django import forms
from .models import Post

class Form(forms.ModelForm):
    content = forms.CharField(
        label_suffix="",
        widget=forms.Textarea(attrs={
            'rows': 5,
            'style': 'width: 100%'
        })
    )
    image = forms.ImageField(
        label_suffix="",
        widget=forms.FileInput(attrs={
            'style': 'width: 100%',
            'class': 'form-control',
        }),
        required=False
    )
    class Meta:
        model = Post
        fields = '__all__'
