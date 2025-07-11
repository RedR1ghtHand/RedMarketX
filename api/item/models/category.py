from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    """
    Item categories, such as:
    - armor
    - weapons
    - tools
    - ammunition
    - utilities
    - wooden
    - structural
    - decorative
    """
    name = models.CharField(max_length=35, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
