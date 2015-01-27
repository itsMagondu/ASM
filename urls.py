from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib.auth.forms import AuthenticationForm

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'siteAdmin.views.home'),
    #url(r'^asm/', include('asm.foo.urls')),

   # Signup 
    (r'^signup/buyer/$', 'siteAdmin.signup.buyer'),
    (r'^signup/seller/$', 'siteAdmin.signup.seller'),

    # for media                                                                                                                                     
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # for django's built in user authentication system The Authentication form dislays the contact page form                  
    (r'^accounts/login/$', 'django.contrib.auth.views.login',
    {'template_name': 'index.html','authentication_form':AuthenticationForm }),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login',
    {'authentication_form':AuthenticationForm }),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
