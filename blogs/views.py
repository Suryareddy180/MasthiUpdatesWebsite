from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import *


# Create your views here.
def posts_by_category(request,category_id):
    # Fetch the posts that belongs to the category with the id category_id
    posts=Blog.objects.filter(category=category_id,status='Published')
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
    'category_id':category_id,
    'category':category,
    }
    return render(request,'posts_by_category.html',context)
