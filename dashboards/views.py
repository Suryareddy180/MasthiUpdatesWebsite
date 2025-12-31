from django.shortcuts import render, redirect
from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .forms import CategoryForm, PostForm, UserForm
from django.template.defaultfilters import slugify
from django.shortcuts import get_object_or_404
from .forms import EditUserForm
# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    # Check if user has any dashboard permissions
    has_permissions = (
        request.user.is_staff or 
        request.user.has_perm('blogs.view_blog') or
        request.user.has_perm('blogs.view_category') or
        request.user.has_perm('auth.view_user')
    )
    
    if not has_permissions:
        return redirect('no_access')
    
    from django.contrib.auth.models import User
    from datetime import datetime, timedelta
    from django.db.models import Count
    
    category_count = Category.objects.all().count()
    post_count = Blog.objects.all().count()
    published_count = Blog.objects.filter(status='Published').count()
    featured_count = Blog.objects.filter(is_featured=True).count()
    draft_count = Blog.objects.filter(status='Draft').count()
    user_count = User.objects.all().count()
    
    # Posts from this week
    week_ago = datetime.now() - timedelta(days=7)
    recent_posts_count = Blog.objects.filter(created_at__gte=week_ago).count()
    
    # Active staff members
    active_staff_count = User.objects.filter(is_staff=True, is_active=True).count()
    
    # Inactive users count
    inactive_users_count = User.objects.filter(is_active=False).count()
    
    # Recent posts for activity feed (last 5)
    recent_posts_list = Blog.objects.all().order_by('-created_at')[:5]
    
    # Top categories by post count
    top_categories = Category.objects.annotate(
        post_count=Count('blog')
    ).order_by('-post_count')[:5]
    
    # Posts created today
    today = datetime.now().date()
    posts_today = Blog.objects.filter(created_at__date=today).count()
    
    context = {
        'category_count': category_count,
        'post_count': post_count,
        'published_count': published_count,
        'featured_count': featured_count,
        'draft_count': draft_count,
        'user_count': user_count,
        'recent_posts': recent_posts_count,
        'active_staff_count': active_staff_count,
        'inactive_users_count': inactive_users_count,
        'recent_posts_list': recent_posts_list,
        'top_categories': top_categories,
        'posts_today': posts_today,
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
    if request.method == 'POST':
        category = get_object_or_404(Category, id=id)
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
def delete_post(request, id):
    if request.method == 'POST':
        post = get_object_or_404(Blog, id=id)
        post.delete()
    return redirect('posts')

@login_required(login_url='login')
def users(request):
    users = auth.get_user_model().objects.all().order_by('-date_joined')
    context = {
        'users': users,
    }
    return render(request, 'dashboards/users.html', context)

@login_required(login_url='login')
def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = UserForm()
    
    context = {
        'form': form,
    }   
    return render(request, 'dashboards/add_user.html', context)
@login_required(login_url='login')
def edit_user(request, id):
    user = get_object_or_404(auth.get_user_model(), id=id)
    if request.method == 'POST':
        form =  EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = EditUserForm(instance=user)
    
    context = {
        'form': form,
        'user': user,
    }   
    return render(request, 'dashboards/edit_user.html', context)

@login_required(login_url='login')
def delete_user(request, id):
    if request.method == 'POST':
        User = auth.get_user_model()
        user = get_object_or_404(User, id=id)
        user.delete()
    return redirect('users')

@login_required(login_url='login')
def no_access(request):
    """View for users without dashboard permissions"""
    context = {
        'admin_email': 'suryareddynallimilli@gmail.com'
    }
    return render(request, 'dashboards/no_access.html', context)

@login_required(login_url='login')

def logout(request):
    auth.logout(request)
    return redirect('login')

