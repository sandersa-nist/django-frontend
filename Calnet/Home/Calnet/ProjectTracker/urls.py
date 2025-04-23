from django.conf.urls import url
from . import views
app_name= 'ProjectTracker'
urlpatterns= [
  url(r'^$',views.index,name='index'),
  ]
