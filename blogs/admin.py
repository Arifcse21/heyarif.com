from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'published_at','updated_on')
    readonly_fields = ('cover_preview',)
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields ={'slug': ('title',)}

    def cover_preview(self, obj):
        return obj.cover_preview

    cover_preview.short_description = 'Cover preview'
    cover_preview.allow_tags = True

admin.site.register(Post, PostAdmin)
