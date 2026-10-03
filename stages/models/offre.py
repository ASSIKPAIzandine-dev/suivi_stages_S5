from django.db import models
from .entreprise import Entreprise
from .competence import Competence

# Create your models here.


class Offre(models.Model):
    """une entreprise susceptible d'accueillir un stagiaire"""

    titre = models.CharField(max_length=150)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    nb_places = models.PositiveBigIntegerField(default=1)

    entreprise = models.ForeignKey(
        Entreprise, on_delete=models.PROTECT, related_name="offres"
    )
    competences = models.ManyToManyField(Competence, related_name="offres")

    class Meta:
        ordering = ["titre"]
        verbose_name = "offre"
        verbose_name_plural = "offres"

    def __str__(self):
        return f"{self.titre} - {self.entreprise.nom}"
