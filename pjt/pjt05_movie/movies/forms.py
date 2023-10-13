from django import forms
from .models import Movie, Comment
from django.core.validators import MaxValueValidator, MinValueValidator, StepValueValidator

class MovieForm(forms.ModelForm):
    genres = [("Comedy", "Comedy"), ("Fantasy", "Fantasy"), ("Romance", "Romance")]
    genre = forms.ChoiceField(choices=genres, widget=forms.Select())
    score = forms.FloatField(
            max_value=5, 
            min_value=0, 
            step_size=0.5,
            validators=[MaxValueValidator(5), MinValueValidator(0), StepValueValidator(0.5)]
        )
    class Meta:
        model = Movie
        fields = ("title", "description", "genre", "score")

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)