from django.forms import ModelForm
from django import forms
from .models import Article


class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    your_lastname = forms.CharField(label='Last Name',max_length=40)
    email = forms.EmailField(label='Email')

class NewArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        exclude=['editor','pub_date']
        widgets={
            'tags':forms.CheckboxSelectMultiple(),
        }
