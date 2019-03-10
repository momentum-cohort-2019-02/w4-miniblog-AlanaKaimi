from django.contrib import admin
from catalog.models import Blogger, BlogPost, Comment

# Register your models here.
admin.site.register(Blogger)
admin.site.register(BlogPost)
admin.site.register(Comment)

# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('user', 'approved')
