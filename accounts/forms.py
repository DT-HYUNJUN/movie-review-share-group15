from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '유저 이름',
            }
        ),
    )
    email = forms.EmailField(
        label='이메일',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': '이메일',
            }
        ),
    )
    first_name = forms.CharField(
        label='이름',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '이름',
            }
        ),
    )
    last_name = forms.CharField(
        label='성',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '성',
            }
        ),
    )    
    password1 = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호',
            }
        ),
    )
    password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호 확인',
            }
        ),
    )
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2',)


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '유저 이름',
            }
        ),
    )
    password = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호',
            }
        ),
    )
    class Meta(AuthenticationForm):
        model = get_user_model
        fields = ('username', 'password')


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = (
            'last_name',
            'first_name',
            'email',
        )