from django.conf.urls import url
from . import views
app_name= 'Measurement'
urlpatterns= [
  url(r'^$',views.index,name='index'),
  ]
