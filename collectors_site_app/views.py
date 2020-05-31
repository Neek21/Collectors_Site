from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt

# html renders/redirects
def index(request):
    if 'user' in request.session:
        return redirect('/success')
    return render(request, 'index.html')

def success(request):
    if 'user' not in request.session:
        return redirect('/')
    logged_user = User.objects.get(id = request.session['id'])
    context = {
        'user' : logged_user,
        'posts' : logged_user.posts.all().order_by('-created_at'),
        'all_posts' : Post.objects.all().order_by('-created_at')
    }
    return render(request, 'profile.html', context)

def my_collection(request):
    logged_user = User.objects.get(id = request.session['id'])
    context ={
        'user' : logged_user,
        'posts' : logged_user.posts.all().order_by('-created_at')
    }

    return render(request, 'my_collection.html', context)

def all_uploads(request):
    return render(request, 'all_user_uploads.html')


# Register
def register(request):
    errors = User.objects.basic_validator(request.POST)

    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')


    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


    new_user = User.objects.create(
        first_name = request.POST['first_name'],
        last_name= request.POST['last_name'],
        email = request.POST['email'],
        password = pw_hash  
    )

    request.session['user'] = new_user.first_name
    request.session['id'] = new_user.id
    return redirect('/success')


# Login
def login(request):
    logged_email = User.objects.filter(email=request.POST['email'])
    errors = {}
    if len(logged_email) == 0:
        errors['email_not_used'] = 'Email is not in use'
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    if len(logged_email) > 0:
        logged_email = logged_email[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_email.password.encode()):
            request.session['user'] = logged_email.first_name
            request.session['id'] = logged_email.id
            return redirect('/success')
        else:
            errors['no_match'] = "Email and password don't match"
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
    return redirect('/')

def dashboard(request):
    return render(request, 'dashboard.html')


# Logout
def logout(request):
    request.session.flush()
    return redirect('/')

# Edits

def edit(request):
    if 'user' not in request.session:
        return redirect('/')

    context ={
        'user' : User.objects.get(id=request.session['id'])
    }

    return render(request, 'edit.html', context)

def edit_process(request):
    logged_user = User.objects.get(id=request.session['id'] )
    errors = {}
    if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
        if logged_user.email != request.POST['email']:
            emailCheck = User.objects.filter(email=request.POST['email'])
            if len(emailCheck) > 0:
                errors['email_in_use'] = 'Email is already in use'
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/edit')
        
        errors = User.objects.edit_validator(request.POST)

        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/edit')

        password = request.POST['new_password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        logged_user.first_name = request.POST['first_name']
        logged_user.last_name = request.POST['last_name']
        logged_user.email = request.POST['email']
        logged_user.bio = request.POST['bio']
        logged_user.password = pw_hash
        logged_user.save()

        return redirect('/success')

    else:
        errors['wrong_pass'] = "Incorrect password."
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/edit')

#Post

def post(request):
    Post.objects.create(
        post_image = request.FILES['post_image'],
        description = request.POST['description'],
        poster = User.objects.get(id=request.session['id'])
    )

    return redirect('/success')

# Viewing all uploads

def all_mine(request):
    return redirect('/all_user_uploads')

def back(request):
    return redirect('/success')
