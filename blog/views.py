from django.shortcuts import render,get_object_or_404
from .models import Post,Author,Tag

# Create your views here.
def start_project(request):
    all_post = Post.objects.order_by('-date')[:3]
    # lattest_posts = sorted(every_post_list,key=get_date)
    # updated_list = lattest_posts[-3:]
    return render(request,"blog/index.html",{"latest_posts":all_post})

def posts(request):
    all_post = Post.objects.all().order_by('-date')
    return render(request,"blog/allPosts.html",{"allPost":all_post})

def individual_posts(request,slug):
    identified_post = get_object_or_404(Post,slug=slug)
    return render(request,"blog/postDetails.html",{"post":identified_post,"post_tag":identified_post.tag.all()})