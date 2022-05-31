from django import forms

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    last_name = forms.CharField(label='Last Name',max_length=40)
    email = forms.EmailField(label='Email')