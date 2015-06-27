from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^add/', 'photo.views.add'),
    url(r'^admin/', 'photo.views.admin'),
    url(r'^upload/', 'photo.views.upload'),
    url(r'^uploader/', 'photo.views.uploader'),
    url(r'^profile/', 'photo.views.profile'),
    url(r'^view/', 'photo.views.view'),
    url(r'^search/', 'photo.views.search'),
    url(r'^subcateg/', 'photo.views.subcategories'),
)
