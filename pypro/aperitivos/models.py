from django.urls import reverse
from django.db import models

class Video(models.Model):    
    slug = models.CharField(max_length=32)
    titulo = models.CharField(max_length=32)
    synthesia_id = models.CharField(max_length=32)

    def get_absolute_url(self):
        return reverse('aperitivos:video', args=(self.slug,))
