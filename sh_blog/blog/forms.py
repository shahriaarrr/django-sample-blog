from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    email = forms.EmailField()
    fullname = forms.CharField()
    phonenumber = forms.IntegerField(required=False)

    def clean_fullname(self):
        name = self.cleaned_data['fullname']
        if name.istitle() == False:
            message = "Error, The first letter of your first and last name must be uppercase."
            raise forms.ValidationError(message)
        return name