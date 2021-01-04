from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils import unique_slug_generator


class Project(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(blank=True, allow_unicode=True)
    api_endpoint = models.URLField()

    def __str__(self):
        return self.name


@receiver(post_save, sender=Project)
def create_unique_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        instance.save()
