from django import forms
from .models import userregistermodel
class userregisterform(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'size':50,'class': 'special'}), required=True,max_length=100 )
    email = forms.CharField(widget=forms.TextInput(attrs={'size':50}), required=True, max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'size':50}), required=True,max_length=100)
    mobile = forms.CharField(widget=forms.TextInput(attrs={'size':50}), required=True,max_length=100)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 52}), required=True,max_length=250)
    city = forms.CharField(widget=forms.TextInput(attrs={'size':50}), required=True,max_length=100)
    state = forms.CharField(widget=forms.TextInput(attrs={'size':50}), required=True,max_length=100)
    status = forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)

    class Meta():
        model = userregistermodel
        fields=['name','email','password','mobile','address','city','state','status']
