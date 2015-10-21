from django.db import models

# Create your models here.

class NewUser(models.Model):
	name		= models.CharField(max_length=50)
	email		= models.EmailField()
	password	= models.CharField(max_length=50)
	timestamp	= models.DateTimeField(auto_now_add=True)