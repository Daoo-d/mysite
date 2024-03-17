from typing import Any
from django.shortcuts import render,get_object_or_404
from .models import Post,Author,Tag
from django.views.generic import ListView,DetailView

# Create your views here.
class PostList(ListView):
    model = Post
    template_name = "blog/allPosts.html"
    ordering = ['-date']
    context_object_name = "allPost"

class StartProject(ListView):
    model = Post
    template_name = "blog/index.html"  
    ordering = ['-date']
    context_object_name = "latest_posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data
      
class IndividualPost(DetailView):
    template_name = "blog/postDetails.html"
    model = Post

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        loaded_obj = self.object
        context["post_tag"] = loaded_obj.tag.all()
        return context
    