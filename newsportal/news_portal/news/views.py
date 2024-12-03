from django.shortcuts import render

# Create your views here.

from datetime import datetime
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post

class BaseView(TemplateView):
    template_name = 'base.html'

class PostsList(ListView):
    model = Post
    ordering = 'post_date_time'
    template_name = 'posts.html'
    context_object_name = 'posts_list'



class PostsDetail(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = "news"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context
