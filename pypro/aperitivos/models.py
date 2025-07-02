from django.urls import reverse
from django.db import models

class Video(models.Model):    
    slug = models.CharField(max_length=64)
    titulo = models.CharField(max_length=64)
    synthesia_id = models.CharField(max_length=64)

    def get_absolute_url(self):
        return reverse('aperitivos:video', args=(self.slug,))
