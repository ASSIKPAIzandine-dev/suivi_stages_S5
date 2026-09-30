from django.db import models
from .personne import Personne

class TuteurEntreprise(Personne):
   
    class Meta:
        ordering = ["nom","prenom"]
        verbose_name = "tuteur"
        verbose_name_plural = "tuteurs"



