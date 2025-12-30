from django.http import HttpResponse
from django.shortcuts import render,redirect

from blogs.models import Category, Blog
from assignments.models import About
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def home(request):
    # Removed forced redirect to dashboard for authenticated users
    # if request.user.is_authenticated and not request.GET.get('public'):
    #     return redirect('dashboard')
    
    featured_posts=Blog.objects.filter(is_featured=True,status='Published').order_by('-created_at','-updated_at')
    posts = Blog.objects.filter(is_featured=False,status='Published').order_by('-created_at','-updated_at')
    
    # Get About info from database
    about = About.objects.first()
   
    context={
        'featured_posts':featured_posts,
        'posts':posts,
        'about': about,

    }
    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
        
    context={
        'form':form
    }
    return render(request, 'register.html',context)

def login(request):
    if request.method == "POST":
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                
                # Handle "Remember Me" functionality
                if not request.POST.get('remember'):
                    # Session expires when browser closes
                    request.session.set_expiry(0)
                else:
                    # Session lasts for 2 weeks (1209600 seconds)
                    request.session.set_expiry(1209600)
                
                # Redirect superusers to Django admin panel
                print(f"DEBUG: User {user.username} logged in. is_superuser: {user.is_superuser}")
                if user.is_superuser:
                    print("DEBUG: Redirecting superuser to /admin/")
                    return redirect('/admin/')
                
                print("DEBUG: Redirecting regular user to dashboard")
                return redirect('dashboard')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'login.html', context)

def terms(request):
    from datetime import datetime
    context = {
        'current_date': datetime.now()
    }
    return render(request, 'terms.html', context)

def logout(request):
    auth.logout(request)
    return redirect('home')
    

