from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post

class PostList(ListView):
    model = Post
    context_object_name = 'posts'

class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'

class PostCreate(CreateView):
    model = Post
    template_name = 'posts/post_create.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post_list')

class PostUpdate(UpdateView):
    model = Post
    template_name = 'posts/post_update.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post_list')


class PostDelete(DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('post_list')
