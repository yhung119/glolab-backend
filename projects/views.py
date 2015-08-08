from django.shortcuts import render
from django.http import HttpResponseRedirect
from projects.models import Category, Project
from projects.form import CategoryForm, ProjectForm
from userpro.models import CompanyProfile
# Create your views here.

def index(request):
	category_list = Category.objects.order_by('-name')[:6]
	context_dict = {'categories':category_list}
	return render(request,
		'projects/projectview.html',
		context_dict)

def add_category(request):
	if request.method=='POST':
		form = CategoryForm(request.POST)

		if  form.is_valid():
			form.save(commit = True)

			return index(request)
		else:
			print form.errors
	else:
		form = CategoryForm()

	return render(request, 'projects/addprojectview.html', {'form':form})


def add_project(request,category_name_slug):
	try:
		cat = Category.objects.get(slug=category_name_slug)
	except Category.DoesNotExist:
		cat = None

	if request.method=='POST':
		form = ProjectForm(request.POST)
		
		if  form.is_valid:
			if cat:

				project = form.save(commit=False)
				project.companyprofile=CompanyProfile.objects.get(company_name=request.user.companyprofile.company_name)
				project.category = cat
				
				project.save()

				return category(request, category_name_slug)
			else:
				print form.errors

	else:
		form = ProjectForm()

	context_dict={'form':form, 'category':cat,'category_name': cat.name, 'slug':category_name_slug}

	return render(request, 'projects/add_project_view.html', context_dict)

def category(request, category_name_slug):

	# Create a context dictionary which we can pass to the template rendering engine.
	context_dict = {}

	try:
		# Can we find a category name slug with the given name?
		# If we can't, the .get() method raises a DoesNotExist exception.
		# So the .get() method returns one model instance or raises an exception.
		categories = Category.objects.all().order_by('name')
		category = Category.objects.get(slug=category_name_slug)
		context_dict['category_name'] = category.name

		# Retrieve all of the associated pages.
		# Note that filter returns >= 1 model instance.
		pages = Project.objects.filter(category=category)

		# Adds our results list to the template context under name pages.
		context_dict['pages'] = pages
		# We also add the category object from the database to the context dictionary.
		# We'll use this in the template to verify that the category exists.
		context_dict['category'] = category
		context_dict['categories']=categories
		context_dict['slug']=category_name_slug

	except Category.DoesNotExist:
		# We get here if we didn't find the specified category.
		# Don't do anything - the template displays the "no category" message for us.
		pass

	# Go render the response and return it to the client.
	return render(request, 'projects/category.html', context_dict)

def project(request, category_name_slug,project_name_slug):

	# Create a context dictionary which we can pass to the template rendering engine.
	context_dict = {}

	try:
		# Can we find a category name slug with the given name?
		# If we can't, the .get() method raises a DoesNotExist exception.
		# So the .get() method returns one model instance or raises an exception.
		project = Project.objects.get(slug=project_name_slug)
		context_dict['project_name'] = project.name

		# We also add the category object from the database to the context dictionary.
		# We'll use this in the template to verify that the category exists.
		context_dict['project'] = project
		context_dict['slug']=project_name_slug
		context_dict['company_name']=project.companyprofile.company_name
		category = Category.objects.get(slug=category_name_slug)
		context_dict['category_name'] = category.name

		# Retrieve all of the associated pages.
		# Note that filter returns >= 1 model instance.
		pages = Project.objects.filter(category=category)

		# Adds our results list to the template context under name pages.
		context_dict['pages'] = pages
		# We also add the category object from the database to the context dictionary.
		# We'll use this in the template to verify that the category exists.
		context_dict['category'] = category
		context_dict['slug']=category_name_slug

	except Project.DoesNotExist and Category.DoesNotExist:
		# We get here if we didn't find the specified category.
		# Don't do anything - the template displays the "no category" message for us.
		pass

	# Go render the response and return it to the client.
	return render(request, 'projects/individual_project_view.html', context_dict)




