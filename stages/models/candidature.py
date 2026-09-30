from django.db import models

# Create your models here.
class Candidature(models.Model):
    """ une entreprise susceptible d'accueillir un stagiaire"""
    statut = models.CharField(max_length=20)
    date_depot = models.DateField()
  


    class Meta:
        ordering = ["date_depot"]
        verbose_name = "candidature"
        verbose_name_plural = "candidature"

        
      
        

