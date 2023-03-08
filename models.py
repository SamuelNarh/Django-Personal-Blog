from django.db import models

# Create your models here.
class Blog(models.Model):
    date = models.DateField()
    message= models.CharField(max_length=200)
    
# Make migrations helps to create the tables you want 
# python manage.py makemigrations
# python manage.py migrate

#  from personal_blog.models import Blog