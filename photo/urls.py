from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^add/', 'photo.views.Add'),
    url(r'^admin/', 'photo.views.Admin'),

)
