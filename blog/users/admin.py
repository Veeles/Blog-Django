from django.contrib import admin
from posts.models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'photo', 'author')

    def delete_queryset(self, request, queryset):
        print('==========================delete_queryset==========================')
        print(queryset)

       

        queryset.delete()

       
        print('==========================delete_queryset==========================')

admin.site.register(Post, PostAdmin)