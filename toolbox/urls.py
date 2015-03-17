
from django.contrib.auth.forms import AuthenticationForm
from django.conf.urls import patterns, include, url
from django.contrib.sitemaps.views import sitemap
from django.conf import settings

from photologue.sitemaps import GallerySitemap, PhotoSitemap

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

sitemaps = {
    'photologue_galleries': GallerySitemap,
    'photologue_photos': PhotoSitemap,
    }


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'siteAdmin.views.home'),
    url(r'^photo/', include('photo.urls')),

   # Signup 
    (r'^signup/buyer/$', 'siteAdmin.signup.buyer'),
    (r'^signup/seller/$', 'siteAdmin.signup.seller'),

    # for media                                                                                                                                     
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # for django's built in user authentication system The Authentication form dislays the contact page form                  
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html' }),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login'),

    # Uncomment the next line to enable the admin:
    url(r'^toolbox/', include(admin.site.urls)),
                       
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
                  
    #Sitemap
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
    name='django.contrib.sitemaps.views.sitemap')
                     
)

