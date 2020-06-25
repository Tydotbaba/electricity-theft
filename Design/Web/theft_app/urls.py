
from django.urls import path
from .views import index, post_current

urlpatterns = [
    path('', index, name="home" ),
    path('post_current/', post_current, name="post_current" ),
]
