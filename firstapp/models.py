from django.db import models

# Create your models here.
class Translation(models.Model):
	english_text = models.CharField(max_length=20)
	spanish_text = models.CharField(max_length=20)
	number_correct = models.IntegerField(default=0)
	number_incorrect = models.IntegerField(default=0)
	def english_translation(self):
		return self.english_text
	def spanish_translation(self):
		return self.spanish_text
	def display_correct(self):
		return number_correct
	def display_incorrect(self):
		return self.number_incorrect
	def __str__(self):
		return self.english_text