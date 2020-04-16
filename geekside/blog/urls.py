from django.urls import path
from .views import (first_view, all_posts, AllPostsView, AllPostsListView,
  PostDetailView, PostCreateView, PostUpdateView, CreatePostFormView,
  CreatePostModelFormView, SignupView)

urlpatterns = [
  path('first_view', first_view, name='blog.my_view'),
  path('', all_posts, name='blog.posts'),
  path('class_based_view', AllPostsView.as_view(), name='blog.post_cbv'),
  path('list_view', AllPostsListView.as_view(), name='blog.list_view'),
  path('post/<int:pk>', PostDetailView.as_view(), name='blog.post'),
  path('new_post', PostCreateView.as_view(), name='blog.new'),
  path('update_post/<int:pk>', PostUpdateView.as_view(), name='blog.update'),
  path('post_form_view', CreatePostFormView.as_view(), name='blog.form_view'),
  path('post_model_form', CreatePostModelFormView.as_view(), name='blog.model_form_view'),
  path('signup', SignupView.as_view(), name='blog.signup')
]
