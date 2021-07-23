from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    email = forms.EmailField()
    fullname = forms.CharField()
    phonenumber = forms.IntegerField(required=False)