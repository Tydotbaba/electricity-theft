from django.db import models

# signal imports
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


# create the data model

class TheftData(models.Model):
	"""
			This is the Theft Data.
				Data types:
						S/No: integer
						Date: date 
						Time: time
						Current1: Float
						Current2: Float
						Total: Float
						Source: Float
						Difference: Float
 	"""
	date = models.DateField(auto_now_add=True)
	time = models.TimeField(auto_now_add=True)
	current1 = models.FloatField()
	current2 = models.FloatField()
	total = models.FloatField()
	source = models.FloatField()
	difference = models.FloatField()
		


class Source(models.Model):
	"""docstring for Source"""
	source = models.FloatField()
		
class Cur1(models.Model):
	"""docstring for Cur1"""
	cur1 = models.FloatField()

class Cur2(models.Model):
	"""docstring for Cur2"""
	cur2 = models.FloatField()




# test data model
class SourceDataModel(models.Model):
	"""docstring for SourceDataModel"""
	source = models.FloatField()
	datetime = models.DateTimeField()
		
class Cur1DataModel(models.Model):
	"""docstring for Cur1DataModel"""
	cur1 = models.FloatField()
	datetime = models.DateTimeField()

class Cur2DataModel(models.Model):
	"""docstring for Cur2DataModel"""
	cur2 = models.FloatField()
	datetime = models.DateTimeField()