from django.conf.urls import include, url
from django.contrib import admin
urlpatterns= [
  url(r'^admin/', admin.site.urls),
  url(r'^Home/',include('Home.urls')),
  url(r'^Repository/',include('Repository.urls')),
  url(r'^ProjectTracker/',include('ProjectTracker.urls')),
  url(r'^CheckStandard/',include('CheckStandard.urls')),
  url(r'^Uncertainties/',include('Uncertainties.urls')),
  url(r'^Measurement/',include('Measurement.urls')),
  url(r'^Preferences/',include('Preferences.urls')),
  url(r'^Help/',include('Help.urls')),
  ]