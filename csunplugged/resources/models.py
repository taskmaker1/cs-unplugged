"""Models for the resources application."""

from django.db import models
from django.urls import reverse
from utils.TranslatableModel import TranslatableModel


class Resource(TranslatableModel):
    """Model for resource in database."""

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=200, default="")
    generator_module = models.CharField(max_length=200)
    thumbnail_static_path = models.CharField(max_length=200)
    copies = models.BooleanField()
    content = models.TextField(default="")

    def get_absolute_url(self):
        """Return the canonical URL for a programming challenge.

        Returns:
            URL as string.
        """
        kwargs = {
            "resource_slug": self.slug
        }
        return reverse("resources:resource", kwargs=kwargs)

    def model_type(self):
        """Text name of model type.

        Returns:
            Name of the model (str).
        """
        return "Resource"

    def __str__(self):
        """Text representation of Resource object.

        Returns:
            Name of resource (str).
        """
        return self.name
