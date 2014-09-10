from django.contrib import admin

# Register your models here.

from blog.models import Post
from blog.models import Comment

class CommentInline(admin.TabularInline):

    model = Comment
    extra = 1


class PostAdmin(admin.ModelAdmin):

    fieldsets = [
        (None,               {'fields': ['title', 'text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    inlines = [CommentInline]

    list_display = ('title', 'pub_date', 'text')
    list_filter = ['pub_date']	


admin.site.register(Post, PostAdmin)
