from django.db import models
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField


class Profile(models.Model):
    """Model definition for MODELNAME."""

    icon = CloudinaryField()
    background = CloudinaryField()
    about_image = CloudinaryField()
    about_text = HTMLField()
    name = models.CharField(max_length = 100)

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return self.name
