from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartProject.as_view(),name="start-project"),
    path("posts", views.PostList.as_view(),name="posts-page"),
    path("posts/<slug>", views.IndividualPost.as_view(),name="post-details")

]