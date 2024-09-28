from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "body",
        "author"
    )
    list_filter =(
        "author",
        "title"
    )


admin.site.register(Post, PostAdmin)
