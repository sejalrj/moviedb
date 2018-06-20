from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from movies.serializers import UserSerializer,MovieSerializer
from movies.models import *	
from rest_framework import generics
# from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class MoviesViewSet(viewsets.ModelViewSet):
	queryset = tblMovies.objects.all()
	serializer_class = MovieSerializer

	def addNewMovie(request,format= None):
		content = {
			'user': unicode(request.user),  # `django.contrib.auth.User` instance.
			'auth': unicode(request.auth),  # None
		}
		return Response(content)
class MovieList(generics.ListAPIView):
	serializer_class = MovieSerializer

	def get_queryset(self):
		print self.kwargs
		moviename = self.kwargs['moviename']
		return tblMovies.objects.filter(name=moviename)

	