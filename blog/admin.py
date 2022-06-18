from django.contrib import admin
from .models import Post


# Register your models here.

class postDB(admin.ModelAdmin):
    list_display = [
        "title", "author", "text", "created_date", "published_date"
    ]


admin.site.register(Post, postDB)
