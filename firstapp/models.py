from django.db import models

# Create your models here.

class User(models.Models):
	username = models.CharField(max_length=20)

class Translation(models.Models):
	english_text = models.CharField(max_length=20)
	spanish_text = models.CharField(max_length=20)

class Correct(models.Models):
	user = models.ForeignKey(User)
	word = models.ForeignKey(Translation)
	number_correct = models.IntegerField(default=0)
	number_incorrect = models.IntegerField(default=0)