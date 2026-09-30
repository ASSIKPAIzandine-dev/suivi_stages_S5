from django.db import models
from .personne import Personne

class Etudiant(Personne):
    matricule = models.CharField(max_length=20)
    promotion = models.CharField()



    class Meta:
        ordering = ["nom","prenom"]
        verbose_name = "etudiant"
        verbose_name_plural = "etudiants"


