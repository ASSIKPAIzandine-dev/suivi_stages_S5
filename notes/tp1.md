Le modèle Entreprise

# 3.1 La spécification

la combinaison de champs qui identifie une entreprise sans ambiguité est  nom et ville de l'entreprise . Deux agences Ecobank (Sokodé et Lomé) sont bien deux
entreprises différentes.

l’adresse mail  est de type EmailField .pas simplement du texte parceque 
l'adresse mail utilise un champ spécifique de type email  plutôt qu'un simple champ de texte brut pour garantir la validité des données, adapter l'expérience mobile et faciliter l'utilisation des navigateurs

le secteur d'activité est du texte libre pour l’instant (plus simple). Une liste imposée serait mieux plus tard,mais coûte plus de temps de maintenance.


Dernière phrase du secrétariat ( on veut la reconnaître tout de suite ). Elle parle de comment l’entreprise s’affiche dans l’admin et ailleurs.

# 3.2 Migrer

## a. la contrainte qui interdit les doublons est unique 

### b. la colonne qui n’a d’équivalent dans aucun champ que nous avons  écrit est la colonne id .elle sort de django, qui l'a crée automatiquement 

### c. Changeons max_length sur un champ, et relanceons makemigrations, par exemple faisons le sur le champs nom
nom = models.CharField(unique=True)
ça nous genère un nouveau fichier stages/migrations/0002_alter_entreprise_nom.py

Maintenant nous avons 2 fichiers et pour revenir en arrière on fera  uv run manage.py migrate stages 0001

### 4. L’administration
### a. L’erreur d’unicité apparaît au moment de validation du  formulaire (pas en tapant, pas plus tard).

### b. Le message est un peu technique donc la secretaire ne peut pas comprendre pour l'instant mais plutard on peut améliorer  

### 5.La première Page
### a. La page d’erreur liste les dossiers où Django a cherché le template. Elle te dit exactement où le fichier aurait dû être.

### b. Non, cette page détaillée ne s’affiche pas en production. Elle dépend de DEBUG =True dans settings.py. En production on met DEBUG = False

### 6. le depot git 
### a. La chose à ignorer : le fichier de base de données `db.sqlite3`.Il contient les données ( entreprises). On ne le met jamais dans Git, car chaque développeur a ses propres données

### b.Les deux fichiers engendrés par uv à commiter :
- pyproject.toml: liste les dépendances
- uv.lock :verrouille les versions exactes


### Restitution
### 1. Pour retrouver le même environnement dans 3 mois :

git clone <ton-repo>
cd suivi_stages
uv sync

### 2. C’est le fichier de migration qui décide de la forme de la table.models.py décrit ce que je veux, la migration traduit ça en SQL, et la base applique ce SQL.

### 3.Les messages d’erreur de Django sont très précis : ils nomment le fichier, la ligne et le
problème exact. Lire jusqu’au bout permet de trouver la solution rapidement.




