from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Category
from django.views import View
from django.views.generic import (ListView, DetailView, CreateView,
  UpdateView, FormView)
from .forms import PostForm, PostModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# ListView -> Lista de de objetos
# DetailView -> Único objeto
# CreateView -> Crear objeto
# UpdateView -> Actualizar un objeto
# DeleteView -> Eliminar un objeto
# FormView -> Procesamiento de formularios

# vista basada en función
def first_view(request): # debe ser probada
  # logica...
  # return HttpResponse("<h1>No vives de ensalada ##</h1>")
  contexto = {
    'food': 'carne'
  }
  return render(request, 'blog/my_template.html', context=contexto)

def all_posts(request):
  contexto = {
    'posts': Post.objects.all(),
    'recent_posts': Post.objects.all().order_by('-created_at')[:2],
    'categories': Category.objects.all().order_by('name')
  }
  return render(request, 'blog/posts.html', context=contexto)

# vistas basadas en clases
class AllPostsView(View):
  
  def get(self, request): # debe probarse
    # lógica
    contexto = {
      'posts': Post.objects.all(),
      'recent_posts': Post.objects.all().order_by('-created_at')[:2]
    }
    return render(request, 'blog/posts.html', context=contexto)

  def post(self, request):
    pass

  def push(self, request):
    pass

class AllPostsListView(ListView):
  model = Post
  template_name = 'blog/posts_list_view.html'

  def get_context_data(self, **kwargs): # debe probarse
    # 1. ejecutar la consulta de todos los registros de Post
    # 2. agregar un nuevo objeto de Post recientes
    context = super().get_context_data(**kwargs)
    # debe estar definido en las HU
    context['recent_posts'] = Post.objects.all().order_by('-created_at')[:2]
    context['categories'] = Category.objects.all().order_by('name')
    return context

class PostDetailView(DetailView):
  model = Post
  template_name = 'blog/post_detail.html'

  # def get_object(self, queryset=None):
  #   # requiere el ID
  #   obj = Post.objects.get(pk=1)
  #   return obj

  def get_context_data(self, **kwargs):
    # también podemos sobrescribir el contexto de la plantilla
    context = super().get_context_data(**kwargs)
    context['recent_posts'] = Post.objects.all().order_by('-created_at')[:2]
    context['categories'] = Category.objects.all().order_by('name')
    return context

@method_decorator(login_required, name='dispatch')
class PostCreateView(CreateView):
  model = Post
  form_class = PostModelForm
  template_name = 'blog/new_post.html'
  success_url = '/'
  # fields = '__all__'
  # fields = ['title', 'text', 'excerpt', 'author', 'related_image']
  # exclude = (...)

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

class PostUpdateView(UpdateView):
  model = Post
  template_name = 'blog/new_post.html' # reutilizo el mismo template ya que el
  # contexto es el mismo :)
  success_url = '/'
  # exclude = ('author',)
  fields = ['title', 'text', 'excerpt', 'is_active']

class CreatePostFormView(FormView):
  form_class = PostForm
  template_name = 'blog/new_post.html'
  success_url = '/'

  def form_valid(self, form):
    # procesar la info validada del formulario
    form.instance.author = self.request.user
    form.save()
    return super().form_valid(form)

class CreatePostModelFormView(FormView):
  form_class = PostModelForm
  template_name = 'blog/new_post.html'
  success_url = '/'

  def form_valid(self, form):
    form.instance.author = self.request.user
    form.save()
    return super().form_valid(form)

class SignupView(FormView):
  form_class = UserCreationForm
  template_name = 'bootstrap4/auth/signup.html'
  success_url = '/login'

  def form_valid(self, form):
    form.save()
    return super().form_valid(form)