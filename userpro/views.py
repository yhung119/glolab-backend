from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from userpro.models import UserProfile, CompanyProfile
from userpro.forms import UserProfileForm, UserForm,CompanyProfileForm,editStudentProfile
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
# Create your views here.


def register(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():

			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			profile.save()

			registered = True
			return HttpResponseRedirect('/')

		else:
			print user_form.errors, profile_form.errors
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request,
		'userpro/register.html',
		{'user_form': user_form, 'profile_form': profile_form, 'registered':registered})

def companyregister(request):
	registered =False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = CompanyProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():

			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			profile.save()

			registered = True

		else:
			print user_form.errors, profile_form.errors
	else:
		user_form = UserForm()
		profile_form = CompanyProfileForm()

	return render(request,
		'userpro/companyregister.html',
		{'user_form': user_form, 'profile_form': profile_form, 'registered':registered})

@login_required
def editprofile(request):
	edit = False
	if request.method == 'POST':
		profile_form = UserProfileForm(data=request.POST)

		if profile_form.is_valid():
			profile = profile_form.save(commit = False)
			profile.user = request.user
			profile.save()
			edit = True
			return HttpResponseRedirect('/')

		else:
			print profile_form.errors
	else:
		profile_form=UserProfileForm()
	return render(request,
		'userpro/useredit.html',
		{'profile_form':profile_form})


@login_required
def editstudentprofile(request):
	if request.method == 'POST':
		form = editStudentProfile(request.POST, instance = request.user)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/")
	else:
		form = UserProfileForm()
	
	return render(request, 'registration/student_profile_edit.html', {'form':form})

def index(request):
	
	# Construct a dictionary to pass to the template engine as its context.
	# Note the key boldmessage is the same as {{ boldmessage }} in the template!
	context_dict = {'boldmessage': "I am bold font from the context"}

	# Return a rendered response to send to the client.
	# We make use of the shortcut function to make our lives easier.
	# Note that the first parameter is the template we wish to use.
	return render(request, 'x.html', context_dict)

def company(request):
	context_dict = {'boldmessage': "I am bold font from the context"}


