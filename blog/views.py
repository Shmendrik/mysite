from django.shortcuts import render

# Create your views here.

from blog.models import Post, Comment

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render
from django.forms import ModelForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]

def add_comment(request, post_id):
	#add new comment to our post
	p = request.POST

	if p.has_key("text") and p["text"]:
		
		# if has no author then name him myself
		author = "Nemo"
		if p["comment_author"]: 
			author = p["comment_author"]
		comment = Comment(post=Post.objects.get(pk=post_id))
		
		# save comment form
		cf = CommentForm(p, instance=comment)
		cf.fields["comment_author"].required = False
		comment = cf.save(commit=False)
		
		# save comment instance
		comment.comment_author = author
		notify = True

		comment.save()	

	return_path  = redirect(request.META.get('HTTP_REFERER','/'))

	return return_path

def main(request):
    full_post_list = Post.objects.all().order_by("-pub_date")
    paginator = Paginator(full_post_list, 10)
	
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
    	comment_list = Comment.objects.filter(post=post)
    	return_path  = request.META.get('HTTP_REFERER','/')
    except Post.DoesNotExist:
        raise Http404

    return render(request, 'blog/detail.html', {
    	'post': post, 
    	'comment_list': comment_list, 
    	'comment_form': CommentForm, 
    	'returner':return_path
    	})
