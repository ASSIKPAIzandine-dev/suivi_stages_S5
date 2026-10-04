Modélisation du domaine

# 1. Un modèle par fichier

## a. No changes detected (Aucun changement détecté). Django n'identifie pas un modèle par le nom du fichier physique dans lequel il se trouve, mais par le nom de sa classe et son appartenance à l'application (via le package models importé dans __init__.py).Une migration ne sert pas à suivre l'organisation de nos fichiers Python, mais uniquement à répercuter les changements de structure de données 



### 2. la parole de la responsable des stages 

### 2.1 


### 2.2 
- Non personne ne doit pas avoir sa propre table ,il est préférable de faire de Personne une classe abstraite (abstract = True en Django).La responsable ne
demande jamais la liste de "toutes les personnes" sans distinction ; elle gère soit des étudiants, soit des tuteurs, soit des enseignants.

- Le tuteur appartient d'abord à une entreprise.La responsable mentionne que l'entreprise désigne un tuteur "parmi ses employés". Un tuteur existe donc dans le système en tant que salarié d'une structure, même s'il n'encadre aucun stage cette année-là. On lie donc le TuteurEntreprise à l'Entreprise .


- Une candidature ne donne lieu qu'à un seul stage, et un stage ne peut pas exister sans candidature. C'est le champ OneToOneField(Candidature) dans le modèle Stage qui l'impose. L'unicité et l'obligation sont appliquées au niveau de la base de données (via une contrainte UNIQUE sur la clé étrangère et une règle NOT NULL), ainsi qu'au niveau applicatif dans Python

- On le garantit en ajoutant la contrainte unique_together = ('etudiant', 'offre') (ou UniqueConstraint) dans la configuration Meta du modèle Candidature.
C'est la base de données qui verifie

- Une chaîne de caractères (CharField) est préférable (ex: "2026").Même si une année ressemble à un nombre, on n'effectue jamais d'opérations mathématiques (addition, multiplication) sur une promotion. pour les statistiques de placement, un regroupement SQL (group_by /.values('promotion').annotate()) fonctionne de la même manière sur du texte ou un entier

- Une liste fermée de choix (via l'attribut choices de Django) . Si on laissait le texte libre, une secrétaire pourrait écrire retenu, une autre Retenue, ou faire une faute de frappe (retenuee) 

- Toutes les relations majeures doivent utiliser on_delete=models.PROTECT.  car Si on utilisait CASCADE, supprimer une entreprise supprimerait ses offres, ses candidatures et ses anciens stages. Avec PROTECT, Django bloque la suppression d'une entité tant que des archives (offres,candidatures, stages) y sont rattachées, protégeant ainsi l'historique complet.


### 3. Lire le SQL 
## a . La migration crée 8 tables au total . les tables qui correspondent aux tables que nous n'avons pas crée sont Les tables comme stages_etudiant_competences et stages_offre_competences .elle existe a cause des champs ManyToManyField.

### b. Non, il n'y a pas de table stages_personne. C'est parfaitement cohérent avec l'utilisation de abstract = True dans la classe Meta de Personne

### c. Elle apparaît sous la forme d'une contrainte d'unicité SQL appelée UNIQUE ("etudiant_id", "offre_id") ou via un index unique (CREATE UNIQUE INDEX ) généré automatiquement au sein de la table  stages_candidature


### d. On constate que Dans le SQL généré pour les clés étrangères (FOREIGN KEY), il n'y a aucune mention de ON DELETE RESTRICT ou ON DELETE CASCADE. Les clés sont créées de manière standard.  C'est Django (au niveau applicatif Python) qui applique et gère lui-même les contraintes PROTECT ou CASCADE, et non la base de données directement . Si une ligne était supprimée directement en SQL (via un client de base de données externe ou un script brut), sans passer par l'ORM de Django, la règle PROTECT ne serait pas déclenchée, ce qui pourrait laisser la base dans un état incohérent avec des lignes orphelines.


### 4. L’administration
### a. Ce qui se passe : Django lève une erreur (ProtectedError) et refuse catégoriquement la suppression en affichant la liste des objets dépendants (les offres).Oui, c'est exactement ce qu'elle voulait. Elle a spécifié qu'on ne devait jamais perdre l'historique d'un stage

### b. L'interface d'administration aurait affiché un écran de confirmationd'alerte listant l'entreprise, mais aussi toutes les offres liées, toutes les candidatures liées à ces offres, et tous les stages issus de ces candidatures. En validant, l'admin aurait tout supprimé en cascade,nettoyant la base de données mais violant définitivement la règle de conservation de l'historique.


### 6. Ce que la base accepte
### a. 
### 1. Offre inversée (se termine avant de commencer) : Acceptée par le shell et la base.
### 2. Offre au titre vide ("") : Acceptée par le shell et la base.
### 3. Doublon de candidature : Refusée (génère une IntegrityError).

### b.
- Le problème commun aux deux premières erreurs : Il s'agit d'un manque de validation des règles métiers

- Qui aurait dû refuser : La base de données de base (comme SQLite) n'analyse pas la cohérence des dates ou si une chaîne est vide par défaut.



### Restitution (20 min)
# 1.On ne peut pas supprimer une candidature qui a donné lieu à un stage, pour ne jamais perdre qui a fait quel stage, où, et avec qui.L’inverse (CASCADE) effacerait le stage en même temps que la candidature (perte d’historique) .


# 2.Les règles on_delete sont appliquées par Django, pas par SQLite.
- Situation : un admin ou un script SQL supprime directement une ligne stages_entreprise alors qu’il reste des offres (offres orphelines), base incohérente.


# 3.La base a refusé la double candidature (contrainte UNIQUE) et accepté les deux autres.
- Différence : unicité = contrainte de schéma ; dates cohérentes / titre non vide = règles métier absentes du modèle.




