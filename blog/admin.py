from django.contrib import admin
from .models import Like,Comment,Post,PostView


admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(PostView)