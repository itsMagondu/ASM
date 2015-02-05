from django.http import HttpResponseRedirect, HttpResponseServerError, HttpResponse, HttpRequest
from django.template import Context, loader,RequestContext
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django import forms

from django.contrib.auth.models import User
from siteAdmin.models import UserProfile


@csrf_exempt
def buyer(request):
    if (request.method == "POST"):
        args = {}
        errors = {}
        errors['form_errors'] = False
        post = request.POST.copy()

        '''GET ALL POSTED DATA FROM FORM'''
        name = post['name']
        errors['name'] = name
        
        username = post['username']
        errors['username'] = username

        email = post['email']
        errors['email'] = email
        
        pass1 = post['password1']
        errors['password1'] = pass1

        pass2 = post['password2']
        errors['password2'] = pass2

        errors['base_url'] = settings.BASE_URL

        if (name == "" ) or (len(name) < 3):
            errors['form_errors'] = True
            errors['firstname_error'] = True
            errors['error'] = "Invalid name"
            return render_to_response('index.html', errors)
        
        elif (username == "" ) or (len(username) < 6):
            errors['form_errors'] = True
            errors['firstname_error'] = True
            errors['error'] = "Minimum length of username is 6 characters"
            return render_to_response('index.html', errors)

        elif (User.objects.filter(username = username)):
            errors['form_errors'] = True
            errors['firstname_error'] = True
            errors['error'] = "Username already taken"
            return render_to_response('index.html', errors)
        
        elif (pass1 != pass2 ):
            errors['form_errors'] = True
            errors['firstname_error'] = True
            errors['error'] = "Password's do not match"
            return render_to_response('index.html', errors)

        elif (email == "" ):
            errors['form_errors'] = True
            errors['email_error'] = True
            errors['error'] = "Email is required to register."
            return render_to_response('index.html', errors)

        elif (User.objects.filter(email = email)):
            errors['form_errors'] = True
            errors['email_error'] = True
            errors['error'] = "Email Address already registered."
            return render_to_response('index.html', errors)

        elif not (validate_email(email)):
            errors['form_errors'] = True
            errors['email_error'] = True
            errors['error'] = "Invalid email adress."
            return render_to_response('index.html', errors)

        
        args['base_url'] = settings.BASE_URL
        args['name'] = name[0].upper() + name[1:len(name)]
        args['username'] = username
        args['email'] = email
        
#check if email is in system before creating user
        if User.objects.filter(email = email):
            errors['form_errors'] = True
            errors['email_error'] = True
            errors['error_message'] = "Email is already registered"
            return render_to_response('index.html', errors)

        user = User.objects.create_user(email, email)
        user.is_active = True
        user.username = username
        user.first_name = name
        user.set_password(pass1)
        user.email = email
        user.save()
        
        u = UserProfile(isBuyer = True)
        u.User = user
        u.canView = True
        u.credit = 0
        u.balance = 0
        
        errors['form_errors'] = True
        errors['error_message'] = "Congratulations!! You have successfully signed up!"
        
        return HttpResponseRedirect(settings.BASE_URL)

#if not post render error
    return HttpResponseServerError("No POST data sent.")

@csrf_exempt
def seller(request):
    if (request.method == "POST"):
        args = {}
        errors = {}
        errors['form_errors'] = False
        post = request.POST.copy()

        '''GET ALL POSTED DATA FROM FORM'''
        name = post['name']
        errors['name'] = name
        
        username = post['username']
        errors['username'] = username

        email = post['email']
        errors['email'] = email
        
        pass1 = post['password1']
        errors['password1'] = pass1

        pass2 = post['password2']
        errors['password2'] = pass2

        country = post['country']
        errors['country'] = country

        occupation = post['occupation']
        errors['occupation'] = occupation

        errors['base_url'] = settings.BASE_URL

        if (name == "" ) or (len(name) < 3):
            errors['form_errors'] = True
            errors['firstname_error'] = True
            errors['error'] = "Invalid name"
            return render_to_response('index.html', errors)
        
        elif (username == "" ) or (len(username) < 6):
            errors['form_errors'] = True
            errors['firstname_error'] = True
            errors['error'] = "Minimum length of username is 6 characters"
            return render_to_response('index.html', errors)

        elif (User.objects.filter(username = username)):
            errors['form_errors'] = True
            errors['firstname_error'] = True
            errors['error'] = "Username already taken"
            return render_to_response('index.html', errors)
        
        elif (pass1 != pass2 ):
            errors['form_errors'] = True
            errors['firstname_error'] = True
            errors['error'] = "Password's do not match"
            return render_to_response('index.html', errors)

        elif (email == "" ):
            errors['form_errors'] = True
            errors['email_error'] = True
            errors['error'] = "Email is required to register."
            return render_to_response('index.html', errors)

        elif (User.objects.filter(email = email)):
            errors['form_errors'] = True
            errors['email_error'] = True
            errors['error'] = "Email Address already registered."
            return render_to_response('index.html', errors)

        elif not (validateEmail(email)):
            errors['form_errors'] = True
            errors['email_error'] = True
            errors['error'] = "Invalid email adress."
            return render_to_response('index.html', errors)

        
        args['base_url'] = settings.BASE_URL
        args['name'] = name[0].upper() + name[1:len(name)]
        args['username'] = username
        args['email'] = email
        
#check if email is in system before creating user
        if User.objects.filter(email = email):
            errors['form_errors'] = True
            errors['email_error'] = True
            errors['error_message'] = "Email is already registered"
            return render_to_response('index.html', errors)

        user = User.objects.create_user(email, email)
        user.is_active = True
        user.username = username
        user.first_name = name
        user.set_password(pass1)
        user.email = email
        user.save()
        
        u = UserProfile(isSeller = True)
        u.User = user
        u.occupation = occupation
        u.isSeller = True
        u.canView = True
        u.credit = 0
        u.balance = 0
        u.country = country
        
        errors['form_errors'] = True
        errors['error_message'] = "Congratulations!! You have successfully signed up!"
        
        return HttpResponseRedirect(settings.BASE_URL)

#if not post render error
    return HttpResponseServerError("No POST data sent.")

