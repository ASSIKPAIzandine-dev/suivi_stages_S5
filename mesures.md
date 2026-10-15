### Restitution

# 1 .C’est le **N+1** : 1 requête pour récupérer les 50 offres, puis 1 (ou 2) requête(s) **par offre** pour charger les relations. Total ≈ 1 + 2×50 = 101. 

# 2.  Règle de choix :
- `select_related` → relations ForeignKey / OneToOne (jointure)
- `prefetch_related` → relations ManyToMany / reverse FK (requête séparée)

# 3. Écrire `/offres/12/` en dur :
1. Si on change l’URL (préfixe, nom de route…), **tous les templates cassent**.
2. On perd la détection d’erreur au rendu (`NoReverseMatch`) : un lien mort n’est découvert que
par un utilisateur.