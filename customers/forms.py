from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordResetForm,
    SetPasswordForm,
)

from .models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Username'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}
    ))


class RegistrationForm(forms.ModelForm):
    first_name = forms.CharField(label='Enter First Name', min_length=4, max_length=150, help_text='Required')
    last_name = forms.CharField(label='Enter Last Name', min_length=4, max_length=150, help_text='Required')
    email = forms.CharField(max_length=50, help_text='Required', error_messages={'required': 'Sorry, you will need an email'})
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'first name'}
        )
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'last name'}
        )
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail'}
        )
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Password'}
        )
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repeat password'}
        )

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match")
        return cd['password1']

    def unique_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Please use another Email, this is already taken')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserEditForm(forms.ModelForm):

    email = forms.EmailField(
        label='Account email (can not be changed)', max_length=50,
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'email', 'readonly': 'readonly'}
        ))
    first_name = forms.CharField(
            label='Firstname', min_length=4, max_length=150,
            widget=forms.TextInput(
                attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'readonly': 'readonly'}
        ))
    last_name = forms.CharField(
        label='Username', min_length=4, max_length=150,
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'last name',}
        ))
    country = forms.CharField(
        label='Username', min_length=4, max_length=150,
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'country'}
        ))

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['email'].required = True

class PasswordEmailForm(PasswordResetForm):
    email = forms.EmailField(max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'email'}
        ))
    
    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email)

        if not user:
            raise forms.ValidationError('Unfortunatley we can not find that email address')

        return email

class PasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New password',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password'}
        )
    )
    new_password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password'}
        )
    )
