from django.db import models

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
		
