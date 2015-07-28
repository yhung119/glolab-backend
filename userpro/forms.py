from django import forms
from django.contrib.auth.models import User
from userpro.models import UserProfile,CompanyProfile

class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'email','first_name','last_name', 'password')

class UserProfileForm(forms.ModelForm):
	username = forms.CharField(required = True)
	email = forms.EmailField(required = True)
	first_name = forms.CharField(required = False)
	last_name = forms.CharField(required = False)

	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name')

	def clean_email(self):
		username = self.cleaned_data.get('username')
		email = self.cleaned_data.get('email')

		if email and User.objects.filter(email=email).exclude(username=username).count():
			raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
		return email

	def save(self, commit=True):
		user=super(RegistrationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']

		if commit:
			user.save()
		return user

class editStudentProfile(forms.ModelForm):
	username = forms.CharField(required=True)
   	email = forms.EmailField(required=True)
  	first_name = forms.CharField(required=False)
   	last_name = forms.CharField(required=False)

   	class Meta:
   	    model = User
   	    fields = ('username', 'email', 'first_name', 'last_name')

   	def clean_email(self):
   		username = self.cleaned_data.get('username')
   		email = self.cleaned_data.get('email')
   		if email and User.objects.filter(email=email).exclude(username=username).count():
   			raise forms.ValidationError('This email address is already in use. Please give another email address.')
   		return email

	def save(self, commit=True):
	    user = super(editStudentProfile, self).save(commit=False)
	    user.email = self.cleaned_data['email']

	    if commit:
	        user.save()

	    return user

class CompanyProfileForm(forms.ModelForm):
	company_name = forms.CharField(max_length=128, required=True)
	description = forms.CharField(label='', 
					widget=forms.Textarea(attrs={'placeholder': 'description','class':"form-control"}))
	class Meta:
		model = CompanyProfile
		fields=('company_name','description','website')
