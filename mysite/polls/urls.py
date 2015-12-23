from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
	# Start to use Django's generic views
	# using pk instead of question_id because generic.DetailView expects
	# primary key values from the URL to be called pk
  url(r'^$', views.IndexView.as_view(), name='index'),
  url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
  url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
  url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
