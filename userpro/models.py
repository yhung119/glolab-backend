from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User,null=True)
	about_me = models.TextField(max_length=450, default='', blank=True)
	
	def __unicode__(self):
		return self.user.username

class CompanyProfile(models.Model):
	user = models.OneToOneField(User)
	company_name=models.CharField(max_length=128)
	description = models.TextField(max_length=100, default='', blank=True)
	website= models.URLField(blank=True)

	def __unicode__(self):
		return self.company_name

