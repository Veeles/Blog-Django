from django import forms

class Register(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.PasswordInput()
