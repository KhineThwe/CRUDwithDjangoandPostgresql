from django.db import models

# Create your models here.
class Details(models.Model):
	name = models.CharField(max_length = 30)
	age = models.IntegerField(max_length = 20)
	address = models.TextField(max_length = 255)