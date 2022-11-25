from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Academic_year


@receiver(post_save, sender=Academic_year)
def after_saving_session(sender, created, instance, *args, **kwargs):
    """Change all academic sessions to false if this is true"""
    if instance.current is True:
        Academic_year.objects.exclude(pk=instance.id).update(current=False)
 
    
