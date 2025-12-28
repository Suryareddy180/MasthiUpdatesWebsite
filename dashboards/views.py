from django.shortcuts import render, redirect
from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .forms import CategoryForm,PostForm
from django.template.defaultfilters import slugify
from django.shortcuts import get_object_or_404
# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    post_count = Blog.objects.all().count()
    published_count = Blog.objects.filter(status='Published').count()
    featured_count = Blog.objects.filter(is_featured=True).count()
    
    context = {
        'category_count': category_count,
        'post_count': post_count,
        'published_count': published_count,
        'featured_count': featured_count,
    }
    return render(request, 'dashboards/dashboard.html', context)

@login_required(login_url='login')
def categories(request):
    categories = Category.objects.all().order_by('-created_at')
    context = {
        'categories': categories,
    }
    return render(request, 'dashboards/categories.html', context)
@login_required(login_url='login')
def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboards/add_category.html', context)

@login_required(login_url='login')
def edit_category(request, id):
    category = Category.objects.get(id=id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'dashboards/edit_category.html', context)
@login_required(login_url='login')
def delete_category(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('categories')

@login_required(login_url='login')
def posts(request):
    posts = Blog.objects.all().order_by('-created_at')
    context = {
        'posts': posts,
    }
    return render(request, 'dashboards/posts.html', context)

@login_required(login_url='login')
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  # temporarily saving the form
            post.author = request.user
            post.save()
            post.slug = slugify(form.cleaned_data['title']) + '-' + str(post.id)  #unique slug
            post.save()

            return redirect('posts')
        else:
            print('form is not valid')
            print(form.errors)
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboards/add_post.html', context)

@login_required(login_url='login')
def edit_post(request, id):
    post = get_object_or_404(Blog, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(form.cleaned_data['title']) + '-' + str(post.id)  # unique slug
            post.save()
            return redirect('posts')
    else:
        form = PostForm(instance=post)
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'dashboards/edit_post.html', context)

@login_required(login_url='login')
def delete_post(request,id):
   post=get_object_or_404(Blog,id=id)
   post.delete()
   return redirect('posts')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

