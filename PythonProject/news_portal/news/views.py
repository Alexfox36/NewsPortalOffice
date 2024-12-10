from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from datetime import datetime
from .forms import PostForm
from .models import Post
from django.views.generic import (TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from .filters import PostFilter

from django.contrib.auth.mixins import LoginRequiredMixin


class BaseView(TemplateView):
    template_name = 'base.html'


class PostsList(ListView):
    model = Post
    ordering = 'post_date_time'
    template_name = 'news.html'
    context_object_name = 'posts_list'
    paginate_by = 10
    login_url = '/login/'
    redirect_field_name = ''

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset
        return context



class PostsDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'single_post'


class PostCreate(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.quantity = 13
        return super().form_valid(form)


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'edit.html'

class PostDelete(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('post_list')


class PostSearch(ListView):
    form_class = PostForm
    model = Post
    template_name = 'search.html'
    context_object_name = 'post_search'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset
        return context