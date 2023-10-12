from django import forms
from .models import Post, Comment

class Form(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author',)

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'placeholder':'댓글을 작성하세요.',
            'style':'width:90%;',
        })
    )
    class Meta:
        model = Comment
        fields = ('content',)