from django import forms
from .models import User

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        
    

'''
    def clean_fullname(self):
        name = self.cleaned_data['fullname']
        if name.istitle() == False:
            message = "Error, The first letter of your first and last name must be uppercase."
            raise forms.ValidationError(message)
        return name
'''