from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
        name = models.CharField(max_length=128, unique=True)
        views = models.IntegerField(default=0)
        likes = models.IntegerField(default=0)
        slug = models.SlugField(unique=True)

        def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super(Category, self).save(*args, **kwargs)

        def __unicode__(self):
                return self.name

class Userprofile(models.Model):
        user = models.OneToOneField(User)

        website = models.URLField(blank=True)
        picture = models.ImageField(upload_to='profile_image',blank=True)

        def __unicode__(self):
                return self.user.username


