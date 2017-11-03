from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'teasite'
urlpatterns = [
    url(r'^$',views.HomeView.as_view(),name='home'),
    url(r'^(?P<pk>[0-9]+)$', views.DetailView.as_view(), name ='detail'),
    url(r'^person/add/$', views.PersonCreate.as_view(), name ='person-add'),
    url(r'^(?P<pk>[0-9]+)/delete/$',views.PersonDelete.as_view(),name='person-delete'),
    url(r'person/(?P<pk>[0-9]+)/$',views.PersonUpdate.as_view(),name='person-update'),
    url(r'^teamail/$',views.TeaMail,name='teamail'),
]

