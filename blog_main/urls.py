"""
URL configuration for blog_main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

import blogs
from . import views
from blogs import views as BlogsViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('category/',include('blogs.urls')),
    #search endpoint - must come BEFORE blogs/<slug> to avoid conflict
    path('blogs/search/',BlogsViews.search , name ='search'),
    path('blogs/<slug:slug>/',BlogsViews.blogs , name ='blogs'),
    path('comment/edit/<int:comment_id>/', BlogsViews.edit_comment, name='edit_comment'),
    path('comment/delete/<int:comment_id>/', BlogsViews.delete_comment, name='delete_comment'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('terms/',views.terms,name='terms'),
    
    # Password Reset URLs
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    path('dashboard/',include('dashboards.urls')),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
