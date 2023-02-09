from django import  forms

""" Formularios de registro de usuarios"""

class RegistrationForm(forms.Form):
    name = forms.CharField()
    images = forms.ImageField(required=True)

class LoginForm(forms.Form):
    username = forms.CharField()

