from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser

# exceptions
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.query import EmptyQuerySet

# import models
from .models import TheftData, Cur1, Cur2, Source, \
Cur1DataModel, Cur2DataModel, SourceDataModel
	
# importing datetime module 
from datetime import datetime

# Create your views here.

# home page
def index(request):
	theft_data = TheftData.objects.all().order_by('date')[::-1]

	context = {
		'theft_data': theft_data,
	}

	return render(request, 'index.html', context)



# get post data
@api_view(['POST'])
@parser_classes([JSONParser])
def post_current(request, format=None):
	"""
	A view that can accept POST requests with JSON content.
	"""

	# check the sender
	if 'cur1' == request.data['sender']:
		# set cur1 in Cur1	
		Cur1.objects.create(
			cur1 = request.data['value']
		)

		Cur1DataModel.objects.create(
			cur1 = request.data['value'],
			datetime = datetime.now()
		)
	elif 'cur2' == request.data['sender']:
		# set cur1 in Cur1	
		Cur2.objects.create(
			cur2 = request.data['value']
		)
		# add cur2 data to Cur2DataModel
		Cur2DataModel.objects.create(
			cur2 = request.data['value'],
			datetime = datetime.now()
		)
	elif 'source' == request.data['sender']:
		# add source data to Source
		Source.objects.create(
			source = request.data['value']
		)
		# add source data to SourceDataModel
		SourceDataModel.objects.create(
			source = request.data['value'],
			datetime = datetime.now()
		)

	# get cur1 object from database
	cur1 = Cur1.objects.all()
	# if the return queryset is empty, set cur1 to None
	if not cur1:
		cur1 = None
	else:
		cur1 = cur1.last().cur1
	
	cur2 = Cur2.objects.all()
	# if the return queryset is empty, set cur2 to None
	if not cur2:
		cur2 = None
	else:
		cur2 = cur2.last().cur2
	
	# get source object from database
	source = Source.objects.all()
	# if the return queryset is empty, set source to None
	if not source:
		source = None
	else:
		source = source.last().source

	
	# create an empty dictionary to hold the data from the various devices
	d = {
			'cur1': cur1,
			'cur2': cur2,
			'source': source,
		}
	
	# set context
	context = {
		'received data': request.data,
		'session': ['{} => {}'.format(key, value) for key, value in d.items()]
	}
	print(context)
	 
	# if source value has not been set, create source session variable
	if cur1 != None and \
	   cur2 != None and \
	   source != None:
		# add data to database
		total = cur1 + cur2
		TheftData.objects.create(
			current1 = cur1,
			current2 = cur2,
			total = total,
			source = source,
			difference = round((source - total), 2))

		print('All set and exists!')   
		
		# delete the data in the three databases
		Cur1.objects.all().delete()
		Cur2.objects.all().delete()
		Source.objects.all().delete()
		
		
	return Response(context)