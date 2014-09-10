from django.shortcuts import render

# Create your views here.

from blog.models import Post

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from django.core.paginator import Paginator, InvalidPage, EmptyPage



# from django.template import RequestContext, loader
# from django.http import HttpResponse
# #detail
# from django.http import Http404
# from django.shortcuts import render
# #comments
# from django.forms import ModelForm
# from django.shortcuts import redirect
# from django.http import HttpResponseRedirect

# #===
# from django.shortcuts import get_object_or_404, render

# from django.core.paginator import Paginator, InvalidPage, EmptyPage
# from django.core.urlresolvers import reverse

# from blog.models import Post
# from blog.models import Comment



def add_comment(request, post_id):
	#add new comment to our post
	return HttpResponse("Comment was added")

def main(request):
    full_post_list = Post.objects.all().order_by("-pub_date")
    paginator = Paginator(full_post_list, 1)
	
    try: 
    	page = request.GET.get('page')
    except ValueError: page = 1

    try:
        full_post_list = paginator.page(page)

    except (InvalidPage, EmptyPage):
        full_post_list = paginator.page(paginator.num_pages)

    template = loader.get_template('blog/index.html')

    return render(request, 'blog/index.html', {
		'full_post_list': full_post_list,
		'page_range': paginator.page_range,
		'error_message': "Something gone wrong.",
		})


def detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)

    except Post.DoesNotExist:
        raise Http404
    return render(request, 'blog/detail.html', {
    	'post': post, 
    	})
