from django.shortcuts import render
from Blogs import models, forms


def blog_posts(request):
    posts = models.BlogPost.objects.all()
    post_list = {'posts': posts}

    return render(request, 'Blogs/blogs.html', context=post_list)


def blog_post_form(request):
    form = forms.BlogForm

    if request.method == 'POST':
        form = forms.BlogForm(request.POST)

        if form.is_valid():
            """ DO STUFF WITH THE FORM DATA HERE """

    return render(request, 'Blogs/blog_form.html', {'form': form})
