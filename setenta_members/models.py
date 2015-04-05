from django.db import models

# Create your models here.
class Members(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100, primary_key=True)
	city = models.CharField(max_length=50)
	semester = models.IntegerField()
	subjects = models.CharField(max_length=50)

class Authorizations(models.Model):
	email = models.EmailField(max_length=100, unique=True)
	key = models.CharField(max_length=200, primary_key=True)
	expirity = models.DateTimeField()

class Admins(models.Model):
	username = models.CharField(max_length=20, primary_key=True)
	password = models.CharField(max_length=200)