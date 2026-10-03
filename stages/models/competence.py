from django.db import models

# Create your models here.
class Competence(models.Model):
    """ une entreprise susceptible d'accueillir un stagiaire"""
    libelle = models.CharField(max_length=20)


    class Meta:
        ordering = ["libelle"]
        verbose_name = "competence"
        verbose_name_plural = "competences"
        

        