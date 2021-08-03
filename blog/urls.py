from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.home, name = "homepage"),
    path("bloggers/", views.blogger, name = "blogger"),
    path("bloggers/<int:id>/", views.get_author_posts, name="author"),
    path("<slug:post>/", views.post_single, name = "post_single"),
]