from django import forms
from django.contrib.auth.models import User
from userpro.models import UserProfile,CompanyProfile
from django.utils.translation import ugettext, ugettext_lazy as _

class UserForm(forms.ModelForm):
	error_messages = {
		'password_mismatch': _("The two password fields didn't match."),
	}
	password1 = forms.CharField(label=_("Password"),
		widget=forms.PasswordInput)
	password2 = forms.CharField(label=_("Password confirmation"),
		widget=forms.PasswordInput,
		help_text=_("Enter the same password as above, for verification."))

	class Meta:
		model = User
		fields = ("username",)

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError(
				self.error_messages['password_mismatch'],
				code='password_mismatch',
			)
		return password2

	def save(self, commit=True):
		user = super(UserForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user
	class Meta:
		model = User
		fields = ('username', 'email','first_name','last_name', )

class UserProfileForm(forms.ModelForm):
	about_me = forms.CharField(required=True)
	picture = forms.ImageField(required=False)

	class Meta:
		model = UserProfile
		fields=('about_me',)


class editStudentProfile(forms.ModelForm):
	username = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	first_name = forms.CharField(required=False)
	last_name = forms.CharField(required=False)

	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name',)

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

class editStudentDetailProfile(forms.ModelForm):
	about_me = forms.CharField(required=False)

	class Meta:
		model = UserProfile
		fields = ('about_me',)

	def save(self, commit=True):
		user = super(editStudentDetailProfile, self).save(commit=False)
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
