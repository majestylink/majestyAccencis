from django.contrib import admin
from .models import  GalleryImage

class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'timestamp',)




# Register your models here.
admin.site.register(GalleryImage, GalleryImageAdmin)  
