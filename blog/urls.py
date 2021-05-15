from django.conf.urls import url
from django.urls import path

from .views import blogView, PostDetailView, add_comment
# <int:year>
urlpatterns = [
    # path('blog/<int:pk>-<str:slug>/', PostDetailView.as_view(), name='post-details'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', PostDetailView.as_view(), name='post-details'),
    path('add-comment/', add_comment, name='add-comment'),
	path('', blogView, name='blog-home'),

]
 
