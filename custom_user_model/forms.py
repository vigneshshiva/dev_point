from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import Custom_user

class UserForm(UserCreationForm):
    username   = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'username',}))
    email      = forms.EmailField(widget=forms.EmailInput(attrs={'class':'email_register','placeholder':'email',}))
    password1  = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    password2  = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'re_type_password'}))
    class Meta:
        model  = Custom_user
        fields = ('username','email','password1','password2')
class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={'class':'emailinput',}))
    class Meta:
        model = Custom_user
        fields = ('email','password')
    # def clean(self):
    #     password = self.cleaned_data['password']
    #     if not authenticate(email=email,password=password):
    #         raise forms.ValidateError("invalid form")
