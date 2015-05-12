from django.http import *
from django.contrib.auth.models import User
from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import datetime

@login_required
def home(request):
    args = {}
    args['base_url'] = settings.BASE_URL
    args['media_url'] = settings.MEDIA_URL
    args['form_errors'] = False
    args['email_error'] = False
    args['error_message'] = ""
    args['isLoggedIn'] = False
    args['username']=request.user.username
    if request.user.is_authenticated():
        args['isLoggedIn'] = True

    return render_to_response("home.html", args)
    

@csrf_exempt
def login(request):
    args = {}
    args['base_url'] = settings.BASE_URL
    args['media_url'] = settings.MEDIA_URL
    args['form_errors'] = False
    args['email_error'] = False
    args['error_message'] = ""
    return render_to_response("index.html", args)
    
