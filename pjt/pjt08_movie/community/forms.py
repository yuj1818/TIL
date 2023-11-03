from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['title', 'movie_title', 'rank', 'content']


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.TextInput)
    class Meta:
        model = Comment
        exclude = ['review', 'user', 'org_comment', 'like_users']
