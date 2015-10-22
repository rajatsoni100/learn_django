from django.db import models

# Create your models here.

class Branch(models.Model):

	SECTION = (
		('A','Section A'),
		('B','Section B'),
	)

	name		= models.CharField(max_length=32)
	code		= models.CharField(max_length=5)
	section		= models.CharField(max_length=1,choices=SECTION)

class NewUser(models.Model):

	BRANCH = (
		('CSE','Computer Science'),
		('IT','Info Tech'),
	)

	name		= models.CharField(max_length=50)
	email		= models.EmailField()
	branch 		= models.ForeignKey(Branch)
	password	= models.CharField(max_length=50)
	timestamp	= models.DateTimeField(auto_now_add=True)

class Advertisement(models.Model):

	title			= models.CharField(max_length=250)
	description 	= models.TextField()
	user 			= models.ForeignKey(NewUser)