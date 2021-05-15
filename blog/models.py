from __future__ import absolute_import

from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings


from django.db.models.signals import pre_save
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE)
    # author = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField()
    header_image = models.ImageField(upload_to='blog/posts/')
    intro = models.TextField(max_length=255, blank=True, null=True)
    body = RichTextUploadingField(config_name='toolbar_Custom')
    vid_file = models.FileField(upload_to='blog/videos', blank=True, null=True, help_text="Upload Video File")
    youtube_video_id = models.CharField(blank=True, null=True, max_length=20, help_text="Youtube Video ID e.g L0I7i_lE5zA. Not Complete Url")
    category = models.ForeignKey("Category", blank=True, null=True, on_delete=models.SET_NULL)
    pub_time = models.DateTimeField("Publish on", default=timezone.now)
    publish = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now= True)


    class Meta: 
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ["-publish", 'updated', 'title']

    def get_absolute_url(self):
        kwargs = {
            #'pk': self.pk,
            'slug': self.slug,
            'year': self.pub_time.year,
            'month': self.pub_time.month,
            'day': self.pub_time.day,
        }
        return reverse('blog:post-details', kwargs=kwargs)

    def get_video_link(self):
        if self.youtube_video_id:
            return "https://www.youtube.com/embed/{}".format(self.youtube_video_id)
        elif self.vid_file:
            return self.vid_file.url
        else:
            return None

    def __str__(self):
        return self.title

class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100, blank=True, null=True)
    # author =  models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,  related_name='user_comments')
    email = models.EmailField(max_length=100, blank=True, null=True)
    text = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    publish = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now= True)
    approved = models.BooleanField(default=False)

    # Metadata
    class Meta: 
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ["-pub_date", 'author']
    # Methods
    def approve(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.text

class Category(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField(null=True, blank=True)

	def __str__(self):
		return str(self.name)

	class Meta:
		verbose_name = "Post Category"
		verbose_name_plural = "Post Categories"


# slug function
def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Category.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

    
def tag_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(tag_pre_save_reciever, sender=Category)
