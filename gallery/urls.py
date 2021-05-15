from django.conf.urls import url
from django.urls import path


from .views import Gallery

urlpatterns = [
    #path('p/<str:slug>/', MainPageDetailView.as_view(), name='page'),
    path('', Gallery.as_view(), name='gallery'),
    ]
    
