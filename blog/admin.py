from django.contrib import admin
from .models import Category,Like,Comment,Post,PostView

admin.site.register(Category)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(PostView)