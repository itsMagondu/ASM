from django.http import *
from django.contrib.auth.models import User
from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import datetime

@csrf_exempt
def home(request):
    args = {}
    args['base_url'] = settings.BASE_URL
    args['form_errors'] = False
    args['email_error'] = False
    args['error_message'] = ""
    return render_to_response("index.html", args)
    
#@login_required
#def home(request):
#    args = {}
#    args['base_url'] = settings.BASE_URL
#    return render_to_response('home.html', args)

