from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.

class GalleryImage(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    file = models.ImageField(help_text="Upload Gallery Image Here")
    sub_title = models.CharField(max_length=100, blank=True, null=True, help_text="The Caption of the Image")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now= False)

    class Meta: 
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery Images'
        ordering = ["-timestamp", ]

    def __str__(self):
        if self.title:
            return self.title
        else:
            return str(self.timestamp)


# slug function
def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = str(instance.file.name).split('/')[-1]
    qs = GalleryImage.objects.filter(title=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

    
def tag_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.title:
        instance.title = create_slug(instance)

pre_save.connect(tag_pre_save_reciever, sender=GalleryImage)