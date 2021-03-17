from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
	posts = Post.objects.all().order_by('-id')
	data = {
		'post_list': posts,
	}
	return render(request, 'core/index.html', data)


def detail(request, id):
	post = Post.objects.get(id=id)
	data = {
		'post': post
	}
	return render(request, 'core/detail.html', data)
