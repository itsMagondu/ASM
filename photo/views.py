from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.conf import settings
from django.http import *

from photo.models import *

# Create your views here.
#@login_required
def Add(request):
    args = {}
    args['base_url'] = settings.BASE_URL
    args['media_url'] = settings.MEDIA_URL
    args['categories']=Category.objects.all()
    args['subcategories']=SubCategory.objects.all()
    
    return render_to_response("upload.html", args)

def Admin(request):
    args = {}
    args['base_url'] = settings.BASE_URL
    args['media_url'] = settings.MEDIA_URL
    return render_to_response("admin.html", args)

@csrf_exempt
@login_required
def upload(request):
    if not (request.method == "POST"):
        return HttpResponseServerError("No POST data sent.")
    
    title = request.POST.get('title',None)
    tags = request.POST.get('tags',None)
    category = request.POST.get('category',None)
    subcategory = request.POST.get('subcategory',None)
    regular = request.POST.get('regular',None)
    supersize = request.POST.get('supersize',None)
    dpi = request.POST.get('dpi',None)
    number = request.POST.get('people_number',None)
    attribute = request.POST.get('people_type',None)

    print category
    print request.user.id
    print dir(request.user)
    
    p = Photo(
        title = title,
        regularImage = regular,
        supersizeImage = supersize,
        dpi = dpi,
        uploaded_by = request.user.userprofile,
        people_in_picture = 1,
        people_attribute = attribute,
        category_id = 1,
        subcategory_id = 1,
        active=True,
        approved = False,
        approved_by = request.user.userprofile,
        )

    p.save()
    #Redirect to ip page with watermared image
    return HttpResponse("Success")
    

def profile(request):
    args = {}
    args['base_url'] = settings.BASE_URL
    args['media_url'] = settings.MEDIA_URL
    return render_to_response("sellerProfile.html", args)

