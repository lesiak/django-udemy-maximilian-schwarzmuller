from django.urls import path

from . import views

urlpatterns = [
    path('', views.starting_page, name='starting-page'),
    path('posts', views.posts_page, name='posts-page'),
    path('posts/<slug:slug>', views.post_details_page, name='post-details-page'),
]
