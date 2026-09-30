from django.db import models

# Create your models here.
class Personne(models.Model):
    """ une entreprise susceptible d'accueillir un stagiaire"""
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    dateNaissance = models.CharField(max_length=80)
    email = models.EmailField()

    
    
    
    class Meta:
        ordering = ["nom"]
        verbose_name = "entreprise"
        verbose_name_plural = "entreprises"
        
    def __str__(self):
        return f"{self.nom} ({self.ville})"
        
    