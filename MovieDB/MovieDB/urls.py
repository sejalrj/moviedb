from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from movies.views import *

from django.contrib import admin
admin.autodiscover()



# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'movies',MoviesViewSet)
# router.register('^movies/(?P<moviename>.+)/$')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MovieDB.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^movies/(?P<moviename>.+)/$', MovieList.as_view()),
)
