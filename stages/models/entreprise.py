from django.db import models


# Create your models here.
class Entreprise(models.Model):
    """une entreprise susceptible d'accueillir un stagiaire"""

    nom = models.CharField(unique=True)
    ville = models.CharField(max_length=80)
    secteur = models.CharField(max_length=80)
    contact = models.EmailField()

    class Meta:
        ordering = ["nom"]
        verbose_name = "entreprise"
        verbose_name_plural = "entreprises"
        constraints = [
            models.UniqueConstraint(fields=["nom", "ville"], name="nom_par_ville")
        ]

    def __str__(self):
        return f"{self.nom} ({self.ville})"
