from django.shortcuts import render

from django.views.generic import ListView, DetailView

from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseServerError


from .models import Post

# Create your views here.


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
"""
# function based views
def home(request):

    posts = Post.objects.all()
    context = {'posts':posts}

    return render(request, 'home.html', context)"""


class BlogDetailView(DetailView):
    
    model = Post
    template_name = 'post_detail.html'

# get single post
def getPostByID(request, pk):

    try:

        post = Post.objects.get(id=pk)
    except:
        return HttpResponseNotAllowed('Page does not exist')
    print(post)
    context = {'post':post}
    return render(request, 'post_detail.html', context)