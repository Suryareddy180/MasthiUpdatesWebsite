from django.contrib import admin
from .models import *
# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = About.objects.count()
        if count >= 1:
            return False
        return True 
    
admin.site.register(About, AboutAdmin)

