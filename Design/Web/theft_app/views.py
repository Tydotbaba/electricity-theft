from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser


from .models import TheftData

# create a data
data = {
	'cur1': None,
	'cur1': None,
	'source': None,
}



# Create your views here.

# home page
# @login_required(login_url='login')
def index(request):
	theft_data = TheftData.objects.all().order_by('time')[::-1]

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
    # set the session variable
    request.session[request.data['sender']] = request.data['value']

   
    # set context
    context = {
    	'received data': request.data,
    	'session': ['{} => {}'.format(key, request.session[key]) for key in request.session.keys()]
    }

     # get session keys
    sessionKeys = request.session.keys()

    # if source value has not been set, create source session variable
    if 'cur1' in sessionKeys and \
     	'cur2' in sessionKeys and \
     	'source' in sessionKeys:
    	# add data to database
    	current1 =  float(request.session.get('cur1'))
    	current2 =  float(request.session.get('cur2'))
    	total = current1 + current2
    	source =  float(request.session.get('source'))
    	TheftData.objects.create(
    		current1 = current1,
    		current2 = current2,
    		total = total,
    		source = source,
    		difference = round((source - total), 2))

    	print('All set and exists!')   
    	
    	# delete the session
    	for key in list(request.session.keys()):
    		del request.session[key]
    	
    return Response(context)

