from blogs.models import Category, Blog
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'category', 'feature_image', 'short_description', 'content', 'status', 'is_featured')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'