from django.shortcuts import render
from .models import Post, Category
from django.views.generic.list import ListView
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView

from django.http import HttpResponseRedirect
from .models import Post, PostComment, Category
from django.views.generic import TemplateView
from core.helpers import themeVersion

# Create your views here.
def blogView(request):
    template_name = "blog/blog_page.html" #.format(themeVersion())
    context = {}
    post_list = Post.objects.all().filter(publish=True).order_by('-pub_time')
    paginator = Paginator(post_list, 12)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context['posts'] = posts
    context['recent'] = post_list[:3]
    #context['categories'] = Category.objects.all()
    return render(request, template_name=template_name, context=context)


class PostDetailView(DetailView):
    template_name = "blog/post_page.html" #.format(themeVersion())
    model = Post
    query_pk_and_slug = True

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        
        post = self.object
        try:
            next_post = post.get_next_by_pub_time()
            # print(next_post.title)
        except Post.DoesNotExist:
            next_post = None
        context['next_post'] = next_post
        try:
            prev_post = post.get_previous_by_pub_time()
        except Post.DoesNotExist:
            prev_post = None
        context['prev_post'] = prev_post
        context['categories'] = Category.objects.all().order_by('name')[:5]
        context['recent'] = Post.objects.all().filter(publish=True).order_by('-pub_time')[:3]
        return context

def add_comment(request):
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        post =  Post.objects.get(pk=post_id)
        next_url = request.POST.get('post_page')        
        email = request.POST.get('email')
        text = request.POST.get('text')
        user = request.user
        try:
            comment = PostComment()
            comment.post = post
            comment.author = user #.profile
            comment.email = email
            comment.text = text
            comment.save()
            # print("*"(10))
        except Exception as e:
            print(e)
        return HttpResponseRedirect(next_url)
    else:
        next_url = request.META.get('HTTP_REFERER')
        print(next_url)
        return HttpResponseRedirect(next_url)

