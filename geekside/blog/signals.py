from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Category

@receiver(post_save, sender=Category)
def disable_category(sender, instance, created, *args, **kwargs):
    if not created:
        instance.post_set.update(is_active=False)

@receiver(post_save, sender=Category)
def enable_category(sender, instance, created, *args, **kwargs):
    if created:
        instance.post_set.update(is_active=True)