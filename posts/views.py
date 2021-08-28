from django.shortcuts import render
from .models import Post

# Create your views here.
def posts(request):
    allposts = Post.objects.all()
    return render(request, 'blog_index.html', {'pts': allposts})

def post(request, pk):
    pt = Post.objects.get(id=pk)
    return render(request, 'posts.html', {'pt':pt})