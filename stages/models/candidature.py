from django.db import models
from .etudiant import Etudiant
from .offre import Offre


# Create your models here.
class Candidature(models.Model):

    statut = models.CharField(max_length=20)
    date_depot = models.DateField(auto_now=True)
    etudiant = models.ForeignKey(
        Etudiant, on_delete=models.PROTECT, related_name="candidatures"
    )
    offre = models.ForeignKey(
        Offre, on_delete=models.PROTECT, related_name="candidatures"
    )

    class Statut(models.TextChoices):
        DEPOSEE = "DEPOSEE", "Déposée"
        RETENUE = "RETENUE", "Retenue"
        REFUSEE = "REFUSEE", "Refusée"

    statut = models.CharField(
        max_length=50,
        choices=Statut,
        default=Statut.DEPOSEE,
    )

    class Meta:
        ordering = ["date_depot"]
        verbose_name = "candidature"
        verbose_name_plural = "candidatures"

        # un étudiant ne candidate jamais deux fois à la même offre
        constraints = [
            models.UniqueConstraint(
                fields=["etudiant", "offre"], name="offre_par_etudiant"
            )
        ]

    def __str__(self):
        return f"Candidature de {self.etudiant} pour {self.offre.titre}"
