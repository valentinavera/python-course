from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
  title = models.CharField(_('título'), max_length=150)
  text = models.TextField(_('texto'))
  excerpt = models.CharField(_('resumen'), max_length=120, blank=True)
  is_active = models.BooleanField(_('activo'), default=True)
  created_at = models.DateTimeField(_('fecha y hora de registro'),
    auto_now_add=True)
  updated_at = models.DateTimeField(_('fecha y hora de última actualización'),
    auto_now=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE, 
    verbose_name=_('autor'))

  class Meta:
    verbose_name = _('publicación')
    verbose_name_plural = _('publicaciones')

  def __str__(self):
    return self.title
