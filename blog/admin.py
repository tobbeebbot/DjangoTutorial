from django.contrib import admin
from .models import Post

# registers Post as a model that the admin view can see/manipulate
admin.site.register(Post) 

