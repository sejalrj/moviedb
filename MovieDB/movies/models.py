from django.db import models
import json

# Create your models here.
class tblMovies(models.Model):
	popularity = models.FloatField()
	director = models.CharField(max_length=50)
	genre = models.CharField(max_length=50)
	imdb_score = models.FloatField()
	name = models.CharField(max_length=50)

	def set_genre(self,genreList):
		self.genre = json.dumps(genreList)

	def get_genre(self):
		return json.loads(self.genreList)