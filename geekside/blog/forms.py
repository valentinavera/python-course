from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from .models import Post

User = get_user_model()

# Formularios base
class PostForm(forms.Form):
  # <input type="text" minlength="5" maxlength="150" />
  title = forms.CharField(min_length=5, max_length=150, label=_('Título'))
  text = forms.CharField(label=_('Texto'), widget=forms.Textarea)
  excerpt = forms.CharField(label=_('Resumen'))
  is_active = forms.BooleanField(label=_('Activo'), initial=True)
  author = forms.ModelChoiceField(label=_('Autor'),
    queryset=User.objects.filter(is_active=True))

  def save(self, *args, **kwargs):
    # lógica de negocio
    # data ya está validada
    # print(self.cleaned_data) # campos validados y limpios
    # print(self.data) # campos sin validar y sin limpiar
    Post.objects.create(**self.cleaned_data)

# Formularios de modelo
class PostModelForm(forms.ModelForm):
  title = forms.CharField(min_length=10, max_length=150)
  stars = forms.IntegerField(min_value=0, max_value=5, label=_('Estrellas'))

  class Meta:
    model = Post
    fields = ('title', 'excerpt', 'text', 'author', 'is_active')
    # exclude = (...)

  def save(self, commit=True): # debe probarse
    # sobrescribe la lógica de registrar en BD del formulario
    # agregamos la lógica que necesitamos en mi funcionalidad
    if self.cleaned_data['stars'] > 3:
      return super().save(commit=commit)
    return None
