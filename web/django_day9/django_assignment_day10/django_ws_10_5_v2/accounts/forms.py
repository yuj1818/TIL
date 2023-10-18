from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, UserChangeForm, PasswordChangeForm

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

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='기존 비밀번호',
        label_suffix='',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'기존 비밀번호'
            }
        )
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].label_suffix = ''
        self.fields['new_password1'].widget.attrs.update({'class':'form-control', 'placeholder':'새 비밀번호'})
        self.fields['new_password2'].label_suffix = ''
        self.fields['new_password2'].widget.attrs.update({'class':'form-control', 'placeholder':'새 비밀번호 (확인)'})

class CustomCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].label_suffix = ''
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].label_suffix = ''
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].label_suffix = ''

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'password1', 'password2')

class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].label_suffix = ''
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].label_suffix = ''
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].label_suffix = ''
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].label_suffix = ''
        self.fields['password'].label_suffix = ''

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')