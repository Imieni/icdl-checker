from django.db import models

# Create your models here.

class BaseModule(models.Model):
	crn = models.CharField(max_length=20)
	firstname = models.CharField(max_length=150)
	lastname = models.CharField(max_length=150)
	email = models.CharField(max_length=30)
	password = models.CharField(max_length=20)
	

class Intermediate(models.Model):
	crn = models.CharField(max_length=20)
	firstname = models.CharField(max_length=150)
	lastname = models.CharField(max_length=150)
	email = models.CharField(max_length=30)
	password = models.CharField(max_length=20)

class BaseMode(models.Model):
	base_id = models.BigIntegerField()
	response = models.CharField(max_length=50)
	response_date = models.DateTimeField(auto_now=True)

class IntermediateMode(models.Model):
	int_id = models.BigIntegerField()
	response = models.CharField(max_length=50)
	response_date = models.DateTimeField(auto_now=True)
