from django.urls import path
from . import views

urlpatterns = [
    path("", views.start_project,name="start-project"),
    path("posts", views.posts,name="posts-page"),
    path("posts/<slug>", views.individual_posts,name="post-details")

]