import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glolab.settings')

import django
django.setup()

from projects.models import Category, Project


def populate():
    python_cat = add_cat('App')

    add_page(cat=python_cat,
        name = "New Tomorrow", description = "You are creating an app called new tomorrow")


    django_cat = add_cat("Web")

    add_page(cat=django_cat,
        name = "10th Key", description = "You are creating an website called 10th Key")


    frame_cat = add_cat("Videos")

    add_page(cat=frame_cat,
        name = "Old Videos", description = "You are creating an video called video")


    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Project.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_page(cat, name, description, views=0):
    p = Project.objects.get_or_create(category=cat, name = name)[0]
    p.description = description
    p.picture = ''
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting creating objects..."
    populate()
