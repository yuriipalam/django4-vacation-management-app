from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from vacation_management_app.models import Account


class RegisterUser(forms.Form):
    email = forms.CharField(label="Email Address",
                            max_length=100, required=True)
    fullname = forms.CharField(
        label="Full Name", max_length=100, required=True)
    password = forms.CharField(
        label="Password", max_length=100, required=True)
    password_repeat = forms.CharField(
        label="Repeat Password", max_length=100, required=True)

    def email_clean(self):
        email = self.cleaned_data['email'].lower()
        try:
            validate_email(email)
        except:
            raise ValidationError("Invalid Email")
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError("Email Already Exists")
        return email

    def password_clean(self):
        password = self.cleaned_data['password']
        if len(password) < 6:
            raise ValidationError(
                "Passwords length should be at least 6 symbols")
        password_repeat = self.cleaned_data['password_repeat']
        if password and password_repeat and password != password_repeat:
            raise ValidationError("Passwords don't match")
        return password

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['email'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        account = Account.objects.create(
            user=user, fullname=self.cleaned_data['fullname'])
        return user
