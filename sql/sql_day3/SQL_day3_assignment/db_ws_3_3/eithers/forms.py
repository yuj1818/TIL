from django import forms
from .models import Question, Comment

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        widgets = {
            'red_team': forms.TextInput,
            'blue_team': forms.TextInput,
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('pick', 'content',)
        widgets = {
            'pick': forms.Select(choices=((True, 'RED TEAM'), (False, 'BLUE TEAM'))),
            'content': forms.TextInput,
        }

