from django.shortcuts import render

# Create your views here.


# home page
# @login_required(login_url='login')
def index(request):
	# if request.user.is_authenticated:
	# 	user_status = 'loggedin'
	# else:
	# 	user_status = 'loggedout'
	# try:
	# 	current_articles = PublishedArticle.objects.all().order_by('-date_published')[:2]
	# 	archived_articles = PublishedArticle.objects.all().order_by('-date_published')[2:]
	# 	context = {
	# 		'head': 'Home',
	# 		'current_articles': current_articles,
	# 		'archived_articles': archived_articles,
	# 		'user_status': user_status
	# 	}
	# except IndexError:
	# 	raise Http404('<h1>Page not found</h1>')
	return render(request, 'index.html', {})