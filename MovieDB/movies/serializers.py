from django.contrib.auth.models import User
from rest_framework import serializers
from movies.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','is_staff','username','password')
        write_only_fields = ('password',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            is_staff= validated_data['is_staff'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = tblMovies
        fields = ('url','popularity','genre','director','imdb_score','name')

    def create(self,data):
    	movie = tblMovies.objects.create(
    		popularity = data['popularity'],
    		director = data['director'],
    		imdb_score = data['imdb_score'],
    		name = data['name']
    		)
    	movie.set_genre(data['genre'])
    	movie.save()
    	return movie
