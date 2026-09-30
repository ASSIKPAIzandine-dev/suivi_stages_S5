from django.db import models

# Create your models here.
class Stage(models.Model):
    sujet = models.CharField(max_length=200)

    class Meta:
        ordering = ["sujet"]
        verbose_name = "stage"
        verbose_name_plural = "stages"

        
    
       