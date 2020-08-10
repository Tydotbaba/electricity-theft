"""This is a middleware.
It helps to store the data from the three devices that shall connec to the the API server.

Data Structure: a dictionary with the following values
	data = {
		cur1: value,
		cur1: value,
		source: value
	}

"""
import json

class TheftDataMiddleware:
	"""
		My Middleware class that adds a data dictionary to to request
	"""
	def __init__(self, get_response):
		self.get_response = get_response
		print(self.get_response)
		self.data = {}

	def __call__(self, request):
		response = self.get_response(request)
		print("Middleware just got called here!")

		# check for post request
		if request.method == 'POST':
			# decode data from the request body
			body = request.body.decode('utf-8')  # in python 3 json.loads only accepts unicode strings 
			body = json.loads(body)
			print(body)

			# update data dictionary
			self.data[body['sender']] = body['value']
			request['dataDict'] = self.data
			response = self.get_response(request)
			return response

		# we got a get request
		return response



