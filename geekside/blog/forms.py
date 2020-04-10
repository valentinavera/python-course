from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from .models import Post

User = get_user_model()

#formularios base
class PostForm(forms.Form):
    #validaciones de los campos
    title = forms.CharField(min_length=5, max_length=150, label=_('Titulo'))
    text = forms.CharField(label=_('Texto'), widget=forms.Textarea)
    excerpt = forms.CharField(label= _('Resumen'))
    is_active = forms.BooleanField(label= _('Activo'))
    author = forms.ModelChoiceField(label=_('Autor'), queryset=User.objects.filter(is_active=True))

    def save(self, *args, **kwargs):
        #lógica de negocio
        #datos validados, sin errores
        #print(self.cleaned_data) #campos validados y limpios
        #print(self.data) #campos sin validar
        Post.objects.create(**self.cleaned_data)

#formularios de modelo: toman los campos directamente de un modelo
class PostModelForm(forms.ModelForm):
    title = forms.CharField(min_length=10)
    stars = forms.IntegerField(max_value=5, min_value=0, label=_('Estrellas'))
    class Meta:
        model = Post
        fields = ('title', 'excerpt', 'text')

    def save(self, commit=True):
        if self.cleaned_data['stars']>3:
            return super().save(commit=commit)
        return None
    