from django.db import models
from django.template.defaultfilters import slugify
from userpro.models import CompanyProfile
# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=128, unique = True)
	slug = models.SlugField(unique=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name

class Project(models.Model):
	category = models.ForeignKey(Category)
	name = models.CharField(max_length=380)
	description = models.CharField(max_length=3000000)
	views = models.IntegerField(default = 0)
	#picture = models.ImageField(upload_to='project_image',blank = True)
	slug = models.SlugField(unique=True)
	companyprofile = models.ForeignKey(CompanyProfile,default=1)	


	def save(self, *args, **kwargs):
		
		self.slug = slugify(self.name)
		super(Project, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name
		