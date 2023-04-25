from django.urls import path

from .views import BlogListView, BlogDetailView, getPostByID #, home

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    #path('post/<int:pk>/', getPostByID, name='post_details'),
    path('', BlogListView.as_view(), name='home'),
    #path('', home, name='home'),
]

