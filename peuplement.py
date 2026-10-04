from stages.models import (
    Entreprise,
    Competence,
    Etudiant,
    TuteurEntreprise,
    EnseignantReferent,
    Offre,
    Candidature,
    Stage,
)
from datetime import date

django = Competence.objects.create(libelle="Django")
react = Competence.objects.create(libelle="React")
sql = Competence.objects.create(libelle="SQL")
sysadmin = Competence.objects.create(libelle="SysAdmin")
# devops = Competence.objects.create(libelle="DevOps")


ecobank_sokode = Entreprise.objects.create(
    nom="Ecobank", ville="Sokodé", secteur="Banque", contact="sokode@ecobank.com"
)
togocom_sokode = Entreprise.objects.create(
    nom="Togocom", ville="Sokodé", secteur="Télécom", contact="sokode@togocom.tg"
)
ceet_lome = Entreprise.objects.create(
    nom="CEET", ville="Lomé", secteur="Énergie", contact="lome@ceet.tg"
)

tuteur1 = TuteurEntreprise.objects.create(
    nom="Folligan",
    prenom="Koffi",
    sexe="M",
    date_naissance="1985-04-12",
    email="k.folligan@ecobank.com",
    entreprise=ecobank_sokode,
)
tuteur2 = TuteurEntreprise.objects.create(
    nom="Amétépé",
    prenom="Yao",
    sexe="M",
    date_naissance="1990-09-23",
    email="y.amatepe@togocom.tg",
    entreprise=togocom_sokode,
)

prof1 = EnseignantReferent.objects.create(
    nom="Adama",
    prenom="Salif",
    sexe="M",
    date_naissance="1978-01-15",
    email="s.adama@ifnti.com",
)
prof2 = EnseignantReferent.objects.create(
    nom="Mensah",
    prenom="Abla",
    sexe="F",
    date_naissance="1983-11-02",
    email="a.mensah@ifnti.com",
)

e1 = Etudiant.objects.create(
    nom="Koffi",
    prenom="Ama",
    sexe="F",
    date_naissance="2003-05-14",
    email="ama.koffi@ifnti.edu",
    matricule="IE202301",
    promotion="2026",
)

e1.competences.add(django, sql)

e2 = Etudiant.objects.create(
    nom="Touré",
    prenom="Ali",
    sexe="M",
    date_naissance="2002-08-20",
    email="ali.toure@ifnti.edu",
    matricule="IE202302",
    promotion="2026",
)

e2.competences.add(react, django)

o1 = Offre.objects.create(
    titre="Développeur Python/Django",
    description="Stage dev",
    date_debut="2026-02-01",
    date_fin="2026-05-31",
    nb_places=2,
    entreprise=ecobank_sokode,
)

o1.competences.add(django, sql)

o2 = Offre.objects.create(
    titre="Administrateur Réseaux",
    description="Stageinfra",
    date_debut="2026-03-01",
    date_fin="2026-06-30",
    nb_places=1,
    entreprise=togocom_sokode,
)
o2.competences.add(sysadmin)

c1 = Candidature.objects.create(etudiant=e1, offre=o1, statut="RETENUE")
c2 = Candidature.objects.create(etudiant=e2, offre=o1, statut="DEPOSEE")

Stage.objects.create(
    sujet="Optimisation de l'application de crédit",
    candidature=c1,
    tuteur=tuteur1,
    enseignant=prof1,
)

print("Base de données peuplée avec succès !")
