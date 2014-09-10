from django.shortcuts import render

# Create your views here.

from blog.models import Post

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from django.core.paginator import Paginator, InvalidPage, EmptyPage


def main(request):
    full_post_list = Post.objects.order_by('-pub_date')[:3]
    paginator = Paginator(full_post_list, 1)

    template = loader.get_template('blog/index.html')

    try: 
    	page = request.GET.get('page')
    except ValueError: page = 1

    try:
        full_post_list = paginator.page(page)

    except (InvalidPage, EmptyPage):
        full_post_list = paginator.page(paginator.num_pages)


    return render(request, 'blog/index.html', {
		'full_post_list': full_post_list,
		'error_message': "Something gone wrong.",
		})


def detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'blog/detail.html', {'post': post, })
