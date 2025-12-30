import copy
from django.template import context

# Patch BaseContext.__copy__ to fix Python 3.14 compatibility
# The issue is that super().__copy__() in Python 3.14 seems to return a super object
# or behaves unexpectedly for BaseContext, causing attribute errors.
def patched__copy__(self):
    # Create new instance without calling __init__
    duplicate = self.__class__.__new__(self.__class__)
    
    # Copy all standard attributes (handles request, template, etc.)
    if hasattr(self, '__dict__'):
        duplicate.__dict__.update(self.__dict__)
    
    # Specific handling for mutable attributes that need shallow copying
    # Django contexts need their own stack of dicts
    if hasattr(self, 'dicts'):
        duplicate.dicts = self.dicts[:]
        
    # render_context implies a separate state context
    if hasattr(self, 'render_context'):
        duplicate.render_context = copy.copy(self.render_context)
        
    return duplicate

# Apply the patch
context.BaseContext.__copy__ = patched__copy__
