from django.contrib import admin
from .models import Entreprise, Competence, Etudiant, TuteurEntreprise,EnseignantReferent, Offre, Candidature, Stage
# Register your models here.


@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
    list_display = ["nom", "ville", "secteur"]
    search_fields = ["nom, ville"]

@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ['libelle']

@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prenom', 'matricule', 'promotion']
    search_fields = ['nom', 'matricule']

@admin.register(TuteurEntreprise)
class TuteurEntrepriseAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prenom', 'entreprise']

@admin.register(EnseignantReferent)
class EnseignantReferentAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prenom']

@admin.register(Offre)
class OffreAdmin(admin.ModelAdmin):
    list_display = ['titre', 'entreprise', 'date_debut', 'nb_places']

@admin.register(Candidature)
class CandidatureAdmin(admin.ModelAdmin):
    list_display = ['etudiant', 'offre', 'statut', 'date_depot']
    # list_filter = ('statut',)
    
@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ['sujet', 'tuteur', 'enseignant']
    



