

from .models import Post
from django.shortcuts import render, get_object_or_404


def post_list(request):
    posts = Post.objects.all()
    return render(request,
                  'main/blog.html',
                  {'posts': posts})




def post_detail(request, id):
    post = get_object_or_404(Post,
                             id=id)
    return render(request,
                  'main/detail_blog.html',
                  {'post': post})