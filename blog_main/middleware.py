from django.shortcuts import redirect
from django.urls import reverse

class SuperuserRedirectMiddleware:
    """
    Middleware to redirect superusers to admin panel after login
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Check if user just logged in and is being redirected to dashboard
        if (request.user.is_authenticated and 
            request.user.is_superuser and 
            response.status_code == 302 and 
            'dashboard' in response.url):
            # Redirect superusers to admin instead
            return redirect('/admin/')
        
        return response
