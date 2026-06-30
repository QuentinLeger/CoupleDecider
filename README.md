# 🏷️ CoupleDecider

> 💡 Une application qui permet de choisir des sujets d'activités et de débats en couple, prenant les envies et le choix de chaque personne et donne une solution plus ou moins équitable, avec un score de compromis entre les 2 envies

<!-- 🛡️ SECTION BADGES (Style Flat-Square pour look Ingénieur) -->
![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)

---

## 🎯 Permet de décider rapidement, et équitablement entre 2 personnes en couple sans prise de décision d'aucun des 2

Texte classique pour présenter le projet. Pour faire un retour à la ligne forcé sans changer de paragraphe, on met deux espaces en fin de ligne.  
Voici la suite du texte sur une nouvelle ligne.

### 🎭 [TITRE 3] Exemples de polices et mises en forme :
* **Texte en Gras** : Pour appuyer sur les mots-clés importants.
* *Texte en Italique* : Pour les notes discrètes ou les traductions.
* ***Gras et Italique*** : Pour une emphase maximale.
* ~~Texte barré~~ : Pratique pour montrer ce qui a changé ou été corrigé.
* `Code en ligne` : Pour citer une variable, un fichier `main.py` ou une fonction `ask_nova()`.

**Raccourci d'action rapide :**
`Raccourci` ➜ **Résultat attendu à l'écran**

---

## ✨ Fonctionnalités 

#### 📝 Fonctionnalités principales
- 🎙️ **Feature 1** — Choisir un thème comme un film, une séries et récupère les envies des 2 personnes
- 🧠 **Feature 2** — L'envoie vers un double agent à travers l'api de Groq pour donner 3 compromis possible
  - Récupère les données et l'envoie a l'API
  - Renvoie 3 compromis possible sous forme JSON
  - 

#### 🔢 [TITRE 4] Liste ordonnée (Idéal pour des étapes)
1. **Étape 1 :** Première action obligatoire.
2. **Étape 2 :** Deuxième action logique.

---

## 🏗️ [TITRE 2] Architecture du Projet (Blocs de Code & Diagrammes)

### 📂 Structure des fichiers
```text
NomDuProjet/
├── backend/
│   ├── agents/
│   │   └── cDecider.py   # Commentaire explicatif aligné
│   ├── config/
│   │   └── database.db   # base SQLite
└── frontend/
    └── main.py           # Interface Streamlit