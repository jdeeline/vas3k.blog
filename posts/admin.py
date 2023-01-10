from django.contrib import admin

from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title", "slug", "type", "created_at",
        "published_at", "comment_count", "view_count",
        "is_visible"
    )


admin.site.register(Post, PostAdmin)
