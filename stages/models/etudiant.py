from django.db import models
from .personne import Personne
from .competence import Competence


class Etudiant(Personne):
    matricule = models.CharField(max_length=20, unique=True)
    promotion = models.CharField(max_length=4)
    competences = models.ManyToManyField(Competence, related_name="etudiants")

    class Meta:
        ordering = ["nom", "prenom"]
        verbose_name = "etudiant"
        verbose_name_plural = "etudiants"
