from django.contrib import admin
from foodieblog.models import Post , Comment

def make_published(modelAdmin, request, queryset):
    queryset.update(status='d')
make_published.short_description = "Mark selected post as published"

# Register models here to have ability to create post from the admin panel.
class PostAdmin(admin.ModelAdmin):
    list_display = ("blog_title", "blog_author", "slug", "status", "created_on")
    list_filter = ("status",)
    search_fields = ["blog_title", "blog_content"]
    prepopulated_fields = {"slug": ("blog_title",)}
    actions = [make_published]

    def make_published(self, request, queryset):
        rows_updated = queryset.update(status='p')
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "body", "post", "created_on", "active")
    list_filter = ("active", "created_on")
    search_fields = ("name", "email", "body")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)



