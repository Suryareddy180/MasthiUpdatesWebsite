from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    #Category CRUD
    path('categories/',views.categories,name='categories'),
    path('add-category/',views.add_category,name='add_category'),
    path('edit-category/<int:id>/',views.edit_category,name='edit_category'),
    path('delete-category/<int:id>/',views.delete_category,name='delete_category'),

    #Post CRUD
    path('posts/',views.posts,name='posts'),
    path('add-post/',views.add_post,name='add_post'),
    path('edit-post/<int:id>/',views.edit_post,name='edit_post'),
    path('delete-post/<int:id>/',views.delete_post,name='delete_post'),

    #User Management
    path('users/',views.users,name='users'),
    path('add-user/',views.add_user,name='add_user'),
    path('edit-user/<int:id>/',views.edit_user,name='edit_user'),
    path('delete-user/<int:id>/',views.delete_user,name='delete_user'),
    
    # No Access Page
    path('no-access/', views.no_access, name='no_access'),
    
    path('logout/',views.logout,name='logout'),

] 