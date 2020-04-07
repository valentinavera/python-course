from django.urls import path
from .views import first_view, all_posts

urlpatterns = [
  path('first_view', first_view, name='blog.my_view'),
  path('', all_posts, name='blog.posts')
]
