from django.shortcuts import render
from django.views import generic

from .models import BlogPost


class ListView(generic.ListView):
    # model = BlogPost
    template_name = 'blog/list_view.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return BlogPost.objects.filter(status='pub').order_by('-date_time_modified')
