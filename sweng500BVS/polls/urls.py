from django.conf.urls import url

from . import views

app_name = 'polls'

urlpatterns = [
	# ex: /polls/
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),


    url(r'^login/$', views.LoginView.as_view(), name='login'),
    # url(r'^login/$', views.LoginView, name='login'),

    # ex: /polls/5/
    # the 'name' value as called by the {$ url $} template tag
    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # ex: /polls/5/results/
	#url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),

    # ex: /polls/5/vote/
	url(r'^(?P<ballot_id>[0-9]+)/vote/$', views.vote, name='vote'),

]