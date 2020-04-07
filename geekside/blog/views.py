from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# vista basada en función
def first_view(request):
  # logica...
  # return HttpResponse("<h1>No vives de ensalada ##</h1>")
  contexto = {
    'food': 'carne'
  }
  return render(request, 'blog/my_template.html', context=contexto)

def all_posts(request):
  contexto = {
    'posts': Post.objects.all(),
    'recent_posts': Post.objects.all().order_by('-created_at')[:2]
  }
  return render(request, 'blog/posts.html', context=contexto)

# vistas basadas en clases
