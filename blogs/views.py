from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import *

from django.db.models import Q


# Create your views here.
def posts_by_category(request,category_id):
    # Fetch the posts that belongs to the category with the id category_id
    posts=Blog.objects.filter(category=category_id,status='Published').order_by('-created_at')
    #Use try except when we want to do some custom action if the category does not exists
    # try:
    #     category=Category.objects.get(id=category_id)
    # except:
    #     #redirect to home page
    #     return redirect('home')
    # Use get_object_or_404 when you want to show 404 error page if the category does not exist
    category=get_object_or_404(Category,id=category_id)

    context={
    'posts':posts,
    'category':category,
    }
    return render(request,'posts_by_category.html',context)

def blogs(request,slug):
    single_post=get_object_or_404(Blog,slug=slug,status='Published')
    context={
        'single_post':single_post,
    }
    return render(request,'blogs.html',context)

def search(request):
    keyword = request.GET.get('keyword', '')
    posts = []
    
    if keyword:
        posts = Blog.objects.filter(
            Q(title__icontains=keyword) | 
            Q(content__icontains=keyword) | 
            Q(short_description__icontains=keyword),
            status='Published'
        )
    
    context = {
        'posts': posts,
        'keyword': keyword,
    }
    return render(request, 'search.html', context)
