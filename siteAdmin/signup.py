from django.template import Context, loader,RequestContext
from django.http import HttpResponseRedirect, HttpResponseServerError, HttpResponse, HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.core.validators import validate_email
from django.core.validators import email_re
from django.shortcuts import render_to_response

from django.contrib.auth.models import User
from asm.siteAdmin.models import UserProfile

@csrf_exempt
def buyer(request):
    if (request.method == "POST"):
        args = {}
        errors = {}
        errors['form_errors'] = False
        post = request.POST.copy()

        '''GET ALL POSTED DATA FROM FORM'''
        firstname = post['firstname']
        errors['firstname'] = firstname
        
        lastname = post['lastname']
        errors['lastname'] = lastname

        
        email = post['email']
        errors['email'] = email
        
        errors['base_url'] = settings.BASE_URL

        if (firstname == "" ) or (len(firstname) < 2):
            errors['base_url'] = settings.BASE_URL
            errors['form_errors'] = True
            errors['firstname_error'] = True
            errors['error'] = "First Name is required to register."
            return render_to_response('index.html', errors)

        elif (email == "" ):
            errors['base_url'] = settings.BASE_URL
            errors['form_errors'] = True
            errors['email_error'] = True
            errors['error'] = "Email is required to register."
            return render_to_response('index.html', errors)

        elif not (validateEmail(email)):
            errors['base_url'] = settings.BASE_URL
            errors['form_errors'] = True
            errors['email_error'] = True
            errors['error'] = "Invalid email adress."
            return render_to_response('index.html', errors)

        elif not (isAddressValid(email)):
            errors['base_url'] = settings.BASE_URL
            errors['form_errors'] = True
            errors['email_error'] = True
            errors['error_message'] = "Valid email address is required to register."
            return render_to_response('index.html', errors)
        
        args['base_url'] = settings.BASE_URL
        args['firstname'] = firstname[0].upper() + firstname[1:len(firstname)]
        args['lastname'] = lastname
        args['email'] = email
        
#check if email is in system before creating user
        if User.objects.filter(email = email):
            errors['form_errors'] = True
            errors['email_error'] = True
            errors['error_message'] = "Email is already registered"
            return render_to_response('index.html', errors)

        user = User.objects.create_user(email, email)
        user.is_active = True
        user.first_name = firstname
        user.last_name = lastname
        user.save()

        base = "http://" + request.get_host() + settings.BASE_URL
        
        """SEND CONFIRMATION EMAIL"""
        sendEmail(firstname, email,account_no,base)
        
        return HttpResponseRedirect(settings.BASE_URL+'/home')

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

        elif not (validateEmail(email)):
            errors['form_errors'] = True
            errors['email_error'] = True
            errors['error'] = "Invalid email adress."
            return render_to_response('index.html', errors)

        elif not (isAddressValid(email)):
            errors['form_errors'] = True
            errors['email_error'] = True
            errors['error_message'] = "Valid email address is required to register."
            return render_to_response('index.html', errors)
        
        args['base_url'] = settings.BASE_URL
        args['firstname'] = firstname[0].upper() + firstname[1:len(firstname)]
        args['lastname'] = lastname
        args['email'] = email
        
#check if email is in system before creating user
        if User.objects.filter(email = email):
            errors['form_errors'] = True
            errors['email_error'] = True
            errors['error_message'] = "Email is already registered"
            return render_to_response('index.html', errors)

        user = User.objects.create_user(email, email)
        user.is_active = True
        user.username = firstname
        user.set_password = pass1
        user.email = email
        user.save()
        
        u = UserProfile(isBuyer = True)
        u.User = user
        u.occupation = occupation
        u.isSeller = True
        u.canView = True
        u.credit = 0
        u.balance = 0
        u.country = country
        
        base = "http://" + request.get_host() + settings.BASE_URL
        
        """SEND CONFIRMATION EMAIL"""
        sendEmail(firstname, email,account_no,base)
        
        return HttpResponseRedirect(settings.BASE_URL+'/home')

#if not post render error
    return HttpResponseServerError("No POST data sent.")
