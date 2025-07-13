from django.contrib import admin
from blog.models import BlogPost
# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
    list_filter = (
        'created_at',
        'update_at',
    )

    search_fields = (
        'title',
    )

admin.site.register(BlogPost, BlogPostAdmin)