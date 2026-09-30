from django.db import models

# Create your models here.
class Offre(models.Model):
    """ une entreprise susceptible d'accueillir un stagiaire"""
    intitule = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    date_debut = models.DateField()
    date_fin = models.DateField()

    class Meta:
        ordering = ["intitule"]
        verbose_name = "offre"
        verbose_name_plural = "offres"
       
       