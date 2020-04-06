from django.contrib import admin
from .models import Post

# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'excerpt', 'is_active', 'author')
  list_filter = ('is_active', 'author')
  # fields = ('title', 'text', 'excerpt')
  exclude = ('is_active',)