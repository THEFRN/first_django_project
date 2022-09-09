from django.shortcuts import render
from django.views import generic

from .models import BlogPost
from  .forms import PostForm


class ListView(generic.ListView):
    # model = BlogPost
    template_name = 'blog/list_view.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return BlogPost.objects.filter(status='pub').order_by('-date_time_modified')


class DetailView(generic.DetailView):
    model = BlogPost
    template_name = 'blog/detail_view.html'
    context_object_name = 'post'
    # context_object_name is automatically named when we use Detail View


class CreatePost(generic.CreateView):
    form_class = PostForm
    template_name = 'blog/create_post.html'
    # needs the get_absolute_url method :))))) for redirection
