from django.conf.urls import patterns, url

from cms import views

urlpatterns = patterns('',
    url(r'^(?P<title>[A-Za-z0-9\-]+)$', views.article, name='article')
)
