from django.db import models
from .candidature import Candidature
from .tuteur_entreprise import TuteurEntreprise
from .enseignant_referent import EnseignantReferent


# Create your models here.
class Stage(models.Model):
    sujet = models.CharField(max_length=200)
    candidature = models.OneToOneField(
        Candidature, on_delete=models.PROTECT, related_name="stage"
    )
    tuteur = models.ForeignKey(
        TuteurEntreprise,
        on_delete=models.PROTECT,
        related_name="stages",
    )
    enseignant = models.ForeignKey(
        EnseignantReferent, on_delete=models.PROTECT, related_name="stages"
    )

    class Meta:
        ordering = ["sujet"]
        verbose_name = "stage"
        verbose_name_plural = "stages"

    def __str__(self):
        return f"Stage : {self.sujet}"
