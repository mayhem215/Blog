
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import request
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def all(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    print(len(posts))
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)
    return render(request, 'blog/all.html', {'page_posts': page_posts})



def stat(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/stat.html', {'post': post})


