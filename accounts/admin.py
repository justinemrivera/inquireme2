from django.contrib import admin
from .models import User
from inquire_me.models import Post

# Register your models here.
admin.site.register(User)
admin.site.register(Post)
