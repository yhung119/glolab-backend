from django import forms
from django.contrib.auth.models import User
from userpro.models import UserProfile,CompanyProfile

class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	student_first_name= forms.CharField(max_length=128, help_text="Please Enter your first name")
	student_last_name= forms.CharField(max_length=128, help_text="LastName")
	about_me = forms.CharField(label='', 
					widget=forms.Textarea(attrs={'placeholder': 'about me','required':'false','class':"form-control"}))
	class Meta:
		model = UserProfile
		fields = ('student_first_name', 'student_last_name','about_me',)

class CompanyProfileForm(forms.ModelForm):
	company_name = forms.CharField(max_length=128, required=True)
	description = forms.CharField(label='', 
					widget=forms.Textarea(attrs={'placeholder': 'description','class':"form-control"}))
	class Meta:
		model = CompanyProfile
		fields=('company_name','description','website')