from django.db import models


# Create your models here.
class Personne(models.Model):
    """une entreprise susceptible d'accueillir un stagiaire"""

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    email = models.EmailField(unique=True)

    class Sexe(models.TextChoices):
        HOMME = "H", "Homme"
        FEMME = "F", "Femme"

    sexe = models.CharField(max_length=10, choices=Sexe)

    class Meta:
        ordering = ["nom", "prenom"]
        verbose_name = "personne"
        verbose_name_plural = "personnes"
        abstract = True

    def __str__(self):
        return f"{self.prenom} {self.nom}"
