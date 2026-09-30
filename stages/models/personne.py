from django.db import models

# Create your models here.
class Personne(models.Model):
    """ une entreprise susceptible d'accueillir un stagiaire"""
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    dateNaissance = models.DateField()
    email = models.EmailField()
    sexe = models.CharField()


    

    class Meta:
        ordering = ["nom","prenom"]
        verbose_name = "personne"
        verbose_name_plural = "personnes"
        abstract = True
        
    # def __str__(self):
    #     return f"{self.nom} ({self.ville})"
        
    