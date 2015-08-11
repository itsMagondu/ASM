from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response,render
from django.conf import settings
from django.http import *

from photo.models import *

import logging
import json

#Logging initilization
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

handler = logging.FileHandler('/tmp/photo.log')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
logger.info('Great. We are now in business')

@login_required
def add(request):
    args = {}
    args['base_url'] = settings.BASE_URL
    args['media_url'] = settings.MEDIA_URL
    args['categories']=Category.objects.all()
    args['subcategories']=SubCategory.objects.all()
    args['isLoggedIn'] = False
    args['username']=request.user.username

    if request.user.is_authenticated():
        args['isLoggedIn'] = True


    return render_to_response("upload.html", args)

@login_required
def admin(request):
    args = {}
    args['base_url'] = settings.BASE_URL
    args['media_url'] = settings.MEDIA_URL
    args['isLoggedIn'] = False
    args['username']=request.user.username
    if request.user.is_authenticated():
        args['isLoggedIn'] = True

    return render_to_response("admin.html", args)

@login_required
def upload(request):
    if not (request.method == "POST"):
        return HttpResponseServerError("No POST data sent.")
    
    title = request.POST.get('title',None)
    tags = request.POST.get('tags',None)
    category = request.POST.get('category',None)
    subcategory = request.POST.get('subcategory',None)
    supersize = request.FILES['supersize']
    regular = request.FILES['regular']
    dpi = request.POST.get('dpi',None)
    number = request.POST.get('people_number',None)
    attribute = request.POST.get('people_type_group',None)
    
    args = {}
    args['base_url'] = settings.BASE_URL
    args['media_url'] = settings.MEDIA_URL
    args['isLoggedIn'] = False
    args['username']=request.user.username
    if request.user.is_authenticated():
        args['isLoggedIn'] = True
    
    try:
        p = Photo(
            title = title,
            regularImage = regular,
            supersizeImage = supersize,
            dpi = dpi,
            uploaded_by = request.user.userprofile,
            people_in_picture = number,
            people_attribute = attribute,
            category_id = category,
            subcategory_id = subcategory,
            active=True,
            approved = False,
            approved_by = request.user.userprofile,
            )
        
        p.save()
        #Redirect to view page with watermaked image
        logger.info('Successfully added image with ID: '+str(p.id))
        args['image'] = p
        args['success'] = "Image uploaded successfully"
        return render_to_response("view-post.html", args)
        #return HttpResponse("Success")
    except Exception, e:
        #Log the error and send it via email
        logger.error('Failed to create image',exc_info=True)
        args['error'] = "An error occured. Please contact the admin"
        return render_to_response("upload.html", args)

@login_required
def profile(request):
    args = {}
    args['base_url'] = settings.BASE_URL
    args['media_url'] = settings.MEDIA_URL
    args['isLoggedIn'] = False
    args['username']=request.user.username
    args['user'] = request.user
    if request.user.is_authenticated():
        args['isLoggedIn'] = True
    args["photos"] = Photo.objects.filter(uploaded_by=request.user)
    return render_to_response("sellerProfile.html", args)

@login_required
def view(request):
    args = {}
    args['base_url'] = settings.BASE_URL
    args['media_url'] = settings.MEDIA_URL
    args['image'] = Photo.objects.filter(uploaded_by=request.user).order_by('-id')[0]
    args['success'] = "Image uploaded successfully"
    args['isLoggedIn'] = False
    args['username']=request.user.username
    if request.user.is_authenticated():
        args['isLoggedIn'] = True

    return render_to_response("view-post.html", args)

@login_required
def uploader(request):
    args = {}
    args['base_url'] = settings.BASE_URL
    args['media_url'] = settings.MEDIA_URL
    args['isLoggedIn'] = False
    args['username']=request.user.username
    args['categories']=Category.objects.all()
    args['subcategories']=SubCategory.objects.all()
    
    if request.user.is_authenticated():
        args['isLoggedIn'] = True
    
    if not (request.method == "POST"):
        return render_to_response("upload-V3.html", args)
    
    title = request.POST.get('title',None)
    tags = request.POST.get('tags',None)
    category = request.POST.get('category',None)
    subcategory = request.POST.get('subcategory',None)
    supersize = request.FILES['supersize']
    regular = request.FILES['regular']
    dpi = request.POST.get('dpi',None)
    number = request.POST.get('people_number',None)
    attribute = request.POST.get('people_type_group',None)
    
    try:
        p = Photo(
            title = title,
            regularImage = regular,
            supersizeImage = supersize,
            dpi = dpi,
            uploaded_by = request.user.userprofile,
            people_in_picture = number,
            people_attribute = attribute,
            category_id = category,
            subcategory_id = subcategory,
            active=True,
            approved = False,
            approved_by = request.user.userprofile,
            )
        
        p.save()
        #Redirect to view page with watermaked image
        logger.info('Successfully added image with ID: '+str(p.id))
        args['image'] = p
        args['success'] = "Image uploaded successfully"
        return render_to_response("view-post.html", args)

    except Exception, e:
        #Log the error and send it via email
        logger.error('Failed to create image',exc_info=True)
        args['error'] = "An error occured. Please contact the admin"
        return render_to_response("upload-V3.html", args)

@login_required
def search(request):
    args = {}
    args['base_url'] = settings.BASE_URL
    args['media_url'] = settings.MEDIA_URL
    args['photos'] = Photo.objects.all().order_by('-id')
    args['isLoggedIn'] = False
    args['username']=request.user.username
    if request.user.is_authenticated():
        args['isLoggedIn'] = True


    return render_to_response("search.html", args)

def subcategories(request):
    
    if request.method == "GET":
        
        category = request.GET.get("id",None)
        
        s = SubCategory.objects.filter(category_id=category).values("id","name")
        return HttpResponse(json.dumps(dict(data=list(s))), content_type="application/json")
    else:
        return HttpResponse("Not found")
