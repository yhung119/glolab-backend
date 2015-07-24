from django import forms
from django.contrib.auth.models import User
from userpro.models import UserProfile

class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput())
	first_name= forms.CharField(max_length=128, help_text="Please Enter your first name")
	last_name= forms.CharField(max_length=128, help_text="LastName")
	class Meta:
		model = User
		fields = ('username', 'email', 'password', 'first_name','last_name')

class UserProfileForm(forms.ModelForm):
	about_me = forms.CharField(label='', 
					widget=forms.Textarea(attrs={'placeholder': 'about me','required':'true','class':"form-control"}))
	class Meta:
		model = UserProfile
		fields = ('about_me',)