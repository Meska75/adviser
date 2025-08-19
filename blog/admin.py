from django.contrib import admin
from blog.models import Post , Category, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class PostAdmin (SummernoteModelAdmin):
    date_hierarchy = "published_date"
    list_display = ("title" , "author" , "counted_view" , "published_status" , "created_date" , "published_date", "login_require")
    list_filter = ('published_status', 'category',)
    ordering = ('created_date',)
    search_fields = ('title',)
    summernote_fields = ('content',)
    readonly_fields = ("counted_view",)

class CommentAdmin (admin.ModelAdmin):
    date_hierarchy = "created_date"
    list_display = ("subject" , "email" , "name" , "approve", "created_date")
    list_filter = ('approve',)
    ordering = ('created_date',)
    search_fields = ('subject',)
    summernote_fields = ('message',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)