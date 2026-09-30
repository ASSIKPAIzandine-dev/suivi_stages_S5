from django.db import models


class Etudiant(Personne):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    dateNaissance = models.DateField()
    email = models.EmailField()
    sexe = models.CharField()


    

    class Meta:
        ordering = ["nom","prenom"]
        verbose_name = "personne"
        verbose_name_plural = "personnes"


