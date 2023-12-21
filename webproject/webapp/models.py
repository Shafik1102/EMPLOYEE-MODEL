from django.db import models
class Employee(models.Model):
	no=models.IntegerField()
	name=models.CharField(max_length=64)
	city=models.CharField(max_length=64)
	mobile=models.IntegerField()
	salary=models.IntegerField()
	expirence=models.IntegerField()
	position=models.CharField(max_length=64)

