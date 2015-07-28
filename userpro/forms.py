from django import forms
from django.contrib.auth.models import User
from userpro.models import UserProfile,CompanyProfile

class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'email','first_name','last_name', 'password')

class UserProfileForm(forms.ModelForm):
	about_me = forms.CharField(label='', 
					widget=forms.Textarea(attrs={'placeholder': 'about me','required':'false','class':"form-control"}))
	class Meta:
		model = UserProfile
		fields = ('about_me',)

class CompanyProfileForm(forms.ModelForm):
	company_name = forms.CharField(max_length=128, required=True)
	description = forms.CharField(label='', 
					widget=forms.Textarea(attrs={'placeholder': 'description','class':"form-control"}))
	class Meta:
		model = CompanyProfile
		fields=('company_name','description','website')