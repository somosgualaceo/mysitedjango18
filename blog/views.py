from django.shortcuts import render , get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

	paginator = Paginator(posts, 8) 
	page = request.GET.get('page')

	try:
		list = paginator.page(page)
	except PageNotAnInteger:
		list = paginator.page(1)
	except EmptyPage:
		list = paginator.page(paginator.num_pages)

	return render(request, 'blog/post_list.html', {'posts': posts ,'posts': list })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
    	a = 1 + 4
    else:
		post.visitas += 1
		post.save()
		return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('blog.views.post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
  			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('blog.views.post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})

class PostDelete(DeleteView):

    template_name = 'blog/delete_post.html'
    model = Post
    success_url = reverse_lazy('post_list')
    context_object_name = 'post'






