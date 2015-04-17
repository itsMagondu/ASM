from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.conf import settings
from django.http import *

from photo.models import *

import logging

#Logging initilization
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

handler = logging.FileHandler('/tmp/photo.log')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
logger.info('Great. We are now in business')

#@login_required
def add(request):
    args = {}
    args['base_url'] = settings.BASE_URL
    args['media_url'] = settings.MEDIA_URL
    args['categories']=Category.objects.all()
    args['subcategories']=SubCategory.objects.all()
    
    return render_to_response("upload.html", args)

def admin(request):
    args = {}
    args['base_url'] = settings.BASE_URL
    args['media_url'] = settings.MEDIA_URL
    return render_to_response("admin.html", args)

@csrf_exempt
@login_required
def upload(request):
    if not (request.method == "POST"):
        return HttpResponseServerError("No POST data sent.")
    
    print request.FILES

    title = request.POST.get('title',None)
    tags = request.POST.get('tags',None)
    category = request.POST.get('category',None)
    subcategory = request.POST.get('subcategory',None)
    supersize = request.FILES['supersize']
    regular = request.FILES['regular']
#    regular = request.POST.get('regular',None)
#    supersize = request.POST.get('supersize',None)
    dpi = request.POST.get('dpi',None)
    number = request.POST.get('people_number',None)
    attribute = request.POST.get('people_type_group',None)
    
    args = {}
    args['base_url'] = settings.BASE_URL
    args['media_url'] = settings.MEDIA_URL

    
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

def profile(request):
    args = {}
    args['base_url'] = settings.BASE_URL
    args['media_url'] = settings.MEDIA_URL
    return render_to_response("sellerProfile.html", args)

def view(request):
    args = {}
    args['base_url'] = settings.BASE_URL
    args['media_url'] = settings.MEDIA_URL
    args['image'] = Photo.objects.all().order_by('-id')[0]
    args['success'] = "Image uploaded successfully"
    return render_to_response("view-post.html", args)

def search(request):
    args = {}
    args['base_url'] = settings.BASE_URL
    args['media_url'] = settings.MEDIA_URL
    args['photos'] = Photo.objects.all().order_by('-id')
    return render_to_response("categoryV2.html", args)
