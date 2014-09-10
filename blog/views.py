from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.template import RequestContext, loader

def main(request):
    template = loader.get_template('blog/index.html')
    
    return render(request, 'blog/index.html', {
		'error_message': "Something gone wrong.",
		})
