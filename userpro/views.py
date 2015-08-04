from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from userpro.models import UserProfile, CompanyProfile
from userpro.forms import UserProfileForm, UserForm,CompanyProfileForm,editStudentProfile,editStudentDetailProfile
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import permission_required, user_passes_test
# Create your views here.


def register(request):
	registered = False
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	if request.method == 'POST':
		user_form = UserForm(request.POST)
		profile_form = UserProfileForm(request.POST)

		if user_form.is_valid() and profile_form.is_valid():

			user = user_form.save()
			
			
			user = user_form.save(commit=False)
			
			user.set_password(user.password)
			user.save()
			g=Group.objects.get(name="student")
			g.user_set.add(user)
			
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


@login_required()
def editstudentprofile(request):
	if request.method == 'POST':
		form = editStudentProfile(request.POST, instance = request.user)
		detail = UserProfileForm(data=request.POST, instance = request.user)
		if form.is_valid() and detail.is_valid():
			user = form.save()
			user.save()
			profile = detail.save(commit=False)
			profile.user=user
			profile.save()
			return HttpResponseRedirect("/")
		else:
			print form.errors() and profile_form.errors()
	else:
		form = editStudentProfile()
		detail = UserProfileForm()
	
	return render(request, 'registration/student_profile_edit.html', {'form':form,'' 'detail': detail})


def companyregister(request):
	registered =False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = CompanyProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():

			user = user_form.save()
			user.set_password(user.password)
			user.save()
			g=Group.objects.get(name="company")
			g.user_set.add(user)
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


def is_student(user):
	return user.groups.filter(name='student').exists()

@user_passes_test(is_student, login_url='/')
def editprofile(request):
	edit = False
	try:
		user_obj = User.Objects.get(user=request.user)
	except:
		user_obj = None
	if request.method == 'POST':
		profile_form = UserProfileForm(data=request.POST, instance = request.user.userprofile)
		user = request.user
		if profile_form.is_valid():

			profile = profile_form.save(commit=False)
			profile.user=request.user
			
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

def is_company(user):
	return user.groups.filter(name='company').exists()
@user_passes_test(is_company,login_url='/')
def editcompanyprofile(request):
	try:
		company_obj=User.objects.get(user=request.user)
	except:
		company_obj=None
	if request.method=="POST":
		profile_form = CompanyProfileForm(data=request.POST, instance = request.user.companyprofile)
		user = request.user
		if profile_form.is_valid():

			profile = profile_form.save(commit=False)
			profile.user=request.user
			
			profile.save()
			edit = True
			return HttpResponseRedirect('/')

		else:
			print profile_form.errors
	else:
		profile_form=CompanyProfileForm()
	return render(request,
		'userpro/companyedit.html',
		{'profile_form':profile_form})
@login_required()
def editstudentprofile(request):
	if request.method == 'POST':
		form = editStudentProfile(request.POST, instance = request.user)
		profile_form = UserProfileForm(data=request.POST, instance = request.user)
		if form.is_valid() and profile_form.is_valid():
			form.save()
			profile = profile_form.save(commit=False)
			
			profile.save()
			return HttpResponseRedirect("/")
		else:
			print form.errors() and profile_form.errors()
	else:
		form = editStudentProfile()
		detail = UserProfileForm()
	
	return render(request, 'registration/student_profile_edit.html', {'form':form, 'detail': detail})


def index(request):
	
	# Construct a dictionary to pass to the template engine as its context.
	# Note the key boldmessage is the same as {{ boldmessage }} in the template!
	

	# Return a rendered response to send to the client.
	# We make use of the shortcut function to make our lives easier.
	# Note that the first parameter is the template we wish to use.
	return render(request, 'student.html', {})


@login_required
def profile(request):
	return render(request,'userpro/profile.html',{})


	







