from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "pages",
        "price",
        "is_available",
        "created_at",
    )
    search_fields = (
        "title",
        "author",
    )
    list_filter = (
        "is_available",
    )
    ordering = (
        "-created_at",
    )

admin.site.register(Book,BookAdmin)
