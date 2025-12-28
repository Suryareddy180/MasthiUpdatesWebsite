from blogs.models import Category, Blog
from django import forms

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title',  'category', 'feature_image', 'short_description', 'content', 'status', 'is_featured')