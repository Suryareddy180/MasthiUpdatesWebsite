from blogs.models import Category, Blog
from assignments.models import About
from django.contrib.auth.models import User


def get_categories(request):
    # Get all categories
    categories = Category.objects.all()
    
    # Calculate site stats
    total_posts = Blog.objects.filter(status='Published').count()
    total_users = User.objects.count()
    total_languages = 8  # Based on the language selector (English + 7 Indian languages)
    
    return {
        'categories': categories,
        'site_stats': {
            'total_posts': total_posts,
            'total_users': total_users,
            'total_languages': total_languages,
        }
    }


def get_about(request):
    about=About.objects.first()
    return dict(about=about)
