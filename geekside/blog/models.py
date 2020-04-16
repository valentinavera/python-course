from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
  name = models.CharField(_('nombre'), max_length=64)
  description = models.TextField(_('descripción'))
  is_active = models.BooleanField(_('activa'), default=True)

  class Meta:
    verbose_name = _('categoría')
    verbose_name_plural = _('categorías')

  def __str__(self):
    return self.name

class Post(models.Model):
  title = models.CharField(_('título'), max_length=150) # varchar
  text = models.TextField(_('texto'))
  excerpt = models.CharField(_('resumen'), max_length=120, blank=True)
  is_active = models.BooleanField(_('activo'), default=True)
  created_at = models.DateTimeField(_('fecha y hora de registro'),
    auto_now_add=True)
  updated_at = models.DateTimeField(_('fecha y hora de última actualización'),
    auto_now=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE, 
    verbose_name=_('autor'))
  # solo almacena la ruta al archivo
  related_image = models.ImageField(_('imágen relacionada'), upload_to='posts/',
    null=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE,
    verbose_name=_('categoría'))

  class Meta:
    verbose_name = _('publicación')
    verbose_name_plural = _('publicaciones')
    # db_table = 'publicaciones'
    # indexes = (models.Index(fields=('excerpt', 'author')))
    # unique_together = ('title', 'author')
    # abstract = True
    # ordering  = ('-created_at',)

  def __str__(self):
    return self.title
