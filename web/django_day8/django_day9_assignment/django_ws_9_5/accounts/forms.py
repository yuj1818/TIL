from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'사용자 이름',
            }
        )
    )
    password = forms.CharField(
        label='비밀번호',
        label_suffix='',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'비밀번호',
            }
        )
    )

class CustomerCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomerCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].label_suffix = ''
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].label_suffix = ''
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].label_suffix = ''

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'password1', 'password2')
