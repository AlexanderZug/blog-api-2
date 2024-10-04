from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "created_at"]
    search_fields = ["title", "author__email"]
    list_filter = ["created_at"]
    date_hierarchy = "created_at"
    list_per_page = 20
    save_on_top = True
    list_display_links = ["author"]
