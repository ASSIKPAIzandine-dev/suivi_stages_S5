# 1. Une vue par fichier

## 2. Trois pages neuves 

### 3. Une feuille de style
### a. Le fichier est placé dans stages/static/stages/style.css.C’est la convention Django : les fichiers statiques d’une app se mettent dans APP/static/APP/.Django les trouve automatiquement grâce à AppDirectoriesFinder

### b.On écrit {% static 'stages/style.css' %} plutôt que /static/stages/style.css parce qu’en production STATIC_URL peut changer (CDN, préfixe de version…). `{% static %}` calcule l’URL correcte. Une URL en dur casse au déploiement

## 4. Compter les requêtes 
## 4.1 La mesure

# a. 13 requetes (6 offres)
formule:1 + 2N (1 pour les offres + N pour les entreprises + N pour les compétences)

# b.connection.queries[-1] contient le dernier SQL brut (un `SELECT` sur la table de liaison M2M). L’ORM transforme chaque accès Python en requête SQL indépendante.

# c. 200 offres → 401 requêtes ; 2000 offres → 4001 requêtes.

### 4.2 La correction Déjà implémentée dans les vues (`select_related` + `prefetch_related`).

# d . Deux outils différents parce que les relations sont de natures différentes :
- `entreprise` = ForeignKey (« vers un ») → jointure → `select_related`
- `competences` = ManyToMany (« vers plusieurs ») → table de liaison → `prefetch_related`

# e. `prefetch_related` ajoute 1 requête, mais remplace **N** requêtes par **1**. Le total passe
de 1+N à 2. Gain énorme dès que N grandit.

### 4.3 Le piège
**Non**, la page détail entreprise n’en souffre pas.
La relation inverse `entreprise.offres` est évaluée **une seule fois**. Django fait une seule requête
`WHERE entreprise_id = …`. Pas de N+1.

## 5. Une panne à diagnostiquer
## a.
** Erreur : **`NoReverseMatch`**.
Elle survient **au chargement de la page** (pendant le rendu du template), ni au démarrage du
serveur, ni au clic.

## b. Avec une adresse en dur (`/offres/12/`), aucune erreur n’apparaît tant qu’on ne clique pas, et même alors on a seulement un 404 peu explicite. On préfère `NoReverseMatch` : l’erreur est **immédiate**, **explicite** et apparaît dès le développement, avant même de déployer.

