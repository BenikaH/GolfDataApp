from django.shortcuts import render
from Blogs import models


def blog_posts(request):
    posts = models.BlogPost.objects.all()
    post_list = {'posts': posts}

    return render(request, 'Blogs/blogs.html', context=post_list),
