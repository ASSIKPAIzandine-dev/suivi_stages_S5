### 5.2 Six requêtes

# 1. Les offres des entreprises situées à Sokodé
Offre.objects.filter(entreprise__ville="Sokodé")

# 2. Les étudiants qui possèdent la compétence « Django »
Etudiant.objects.filter(competences__libelle="Django")

# 3. Les candidatures d’un étudiant donné 
from stages.models import Etudiant 
e1 = Etudiant.objects.first()
e1.candidatures.all()


# 4. Le nombre de candidatures retenues (sans charger en mémoire)
Candidature.objects.filter(statut="RETENUE").count()

# 5. Les stages dont l’offre vient d’une entreprise de Sokodé
Stage.objects.filter(candidature__offre__entreprise__ville="Sokodé")

# 6. Les offres qui demandent au moins une compétence que possède un étudiant donné (e1)
Offre.objects.filter(competences__in=e1.competences.all()).distinct()


