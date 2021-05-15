from django.contrib import admin
from .models import Post,  Category, PostComment

from import_export import resources
from import_export.admin import ImportExportModelAdmin


class PostAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'author', 'publish', 'pub_time', 'category', )
    search_fields = ['author', 'title', 'updated', 'body']
    list_filter = [ 'author', 'publish', 'pub_time', 'updated', 'category' ]
    prepopulated_fields = {"slug": ("title",)}

class PostCommentResource(resources.ModelResource):
    class Meta:
        model = PostComment
        fields = ('post', 'author', 'pub_date', 'publish', )
        export_order = ('post', 'author', 'pub_date', 'publish',)

class PostCommentAdmin(ImportExportModelAdmin):
    resource_class = PostCommentResource
    list_display = ['post', 'author', 'pub_date', 'publish', ]
    search_fields = ['post', 'author', 'pub_date', 'publish',]
    list_filter = ['pub_date', 'author', 'publish',] 


class CategoryAdmin(admin.ModelAdmin):
    list_display = ( '__str__', )
    search_fields = ['__str__',]
    #list_filter = [ 'pub_time', 'updated',]
    prepopulated_fields = {"slug": ("name",)}
    
    
# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(PostComment, PostCommentAdmin)
admin.site.register(Category, CategoryAdmin)
