from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.conf import settings

# Create your views here.
#@login_required
def Add(request):
    args = {}
    args['base_url'] = settings.BASE_URL
    args['media_url'] = settings.MEDIA_URL
    return render_to_response("upload.html", args)

def Admin(request):
    args = {}
    args['base_url'] = settings.BASE_URL
    args['media_url'] = settings.MEDIA_URL
    return render_to_response("admin.html", args)

def upload(request):
    pass

def profile(request):
    args = {}
    args['base_url'] = settings.BASE_URL
    args['media_url'] = settings.MEDIA_URL
    return render_to_response("sellerProfile.html", args)

