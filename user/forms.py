from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django import forms

from user.models import Profile


class UserLoginForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(UserLoginForm, self).clean()

        login = cleaned_data['login']
        password = cleaned_data['password']
        self.user = authenticate(username=login, password=password)
        if self.user is None:
            raise forms.ValidationError('Wrong user or password!')
        return cleaned_data


class UserCreateForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Again', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        help_texts = {
            'username': None
        }

    def clean_login(self):
        login = self.cleaned_data['username']
        if User.objects.filter(username=login).exists():
            raise forms.ValidationError('Username exists')
        return login

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email exists')
        return email

    def clean(self):
        cleaned_data = super().clean()
        pass_one = cleaned_data['password']
        pass_two = cleaned_data['password2']
        if not pass_one == pass_two:
            raise forms.ValidationError("Invalid password")
        return cleaned_data


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']
