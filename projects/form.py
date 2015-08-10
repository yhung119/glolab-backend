from django import forms
from projects.models import Category, Project
from userpro.models import CompanyProfile
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField

class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=128, help_text="Enter the Category")
	slug = forms.CharField(widget=forms.HiddenInput(), required = False )

	class Meta:
		model = Category
		fields=('name',)

class ProjectForm(forms.ModelForm):
	name = forms.CharField(max_length=128, help_text="Enter the name of project")
	description = forms.CharField(max_length=100000, help_text="description of your project")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	picture = forms.ImageField(
        label='Select a file',required=False,
	)
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)
	
	class Meta:
		model = Project
		fields= ('name', 'description', 'picture',)

