from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import BlogPost
from .serializers import BlogPostSerializer

def home(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'home.html', {'blog_posts': blog_posts})

def detail(request, post_id):
    blog_post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, 'detail.html', {'blog_post': blog_post})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

class BlogPostListCreateAPIView(ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogPostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
