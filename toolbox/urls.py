
from django.contrib.auth.forms import AuthenticationForm
from django.conf.urls import patterns, include, url
from django.contrib.sitemaps.views import sitemap
from django.conf import settings

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'siteAdmin.views.home'),
    url(r'^photo/', include('photo.urls')),
    
    # Signup 
    (r'^signup/buyer/$', 'siteAdmin.signup.buyer'),
    (r'^signup/seller/$', 'siteAdmin.signup.seller'),
    
    # for media                                                                                                                                     
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
        
    # for django's built in user authentication system The Authentication form dislays the contact page form                  
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html' }),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login'),
    
    url(r'^toolbox/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),                       
    
)

