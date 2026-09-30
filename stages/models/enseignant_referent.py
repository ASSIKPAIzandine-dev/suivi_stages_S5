from django.db import models
from .personne import Personne

class EnseignantReferent(Personne):

    class Meta:
        ordering = ["nom","prenom"]
        verbose_name = "enseignant"
        verbose_name_plural = "enseignants"


