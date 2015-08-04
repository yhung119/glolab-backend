from django.shortcuts import render
from django.http import HttpResponseRedirect
from projects.models import Category, Project
# Create your views here.

def index(request):
	category_list = Project.objects.order_by('-views')[:6]
	context_dict = {'categories':category_list}
	return render(request,
		'projects/projectview.html',
		context_dict)



