# Chemistry Lib 🧪

Une bibliothèque Python légère pour modéliser des atomes, des molécules et des réactions chimiques.

## 📋 Description

**Chemistry Lib** est un package Python conçu pour simplifier la manipulation de données chimiques. Il permet de créer des représentations atomiques, de construire des molécules et de gérer des utilitaires de réaction de base.

Ce projet a été conçu pour mettre en pratique les standards de packaging Python modernes, la programmation orientée objet et les tests unitaires avec `pytest`.

## 🚀 Fonctionnalités

* **Gestion des atomes :** Création d'atomes avec leurs propriétés (symbole, numéro atomique, masse).
* **Construction de molécules :** Assemblage d'atomes pour former des molécules.
* **Utilitaires de réaction :** Outils pour gérer la logique chimique.
* **Fiabilité :** Code couvert à 100% par des tests unitaires via `pytest`.

## 🛠 Installation

Cloner le dépôt:
```bash
git clone https://github.com/elisakaing/chemistry_lib.git
cd chemistry_lib
```

Initialisation du projet:
```bash
pip install -e .
```

## ✅ Lancer les tests
```bash
# Assurez-vous d'abord d'avoir installé pytest
pip install pytest
```
```bash
# Lancer tous les tests
pytest tests
```

## 📂 Structure du projet
```
chemistry_lib/
├── chempkg/           # Code source du package
│   ├── __init__.py
│   ├── atom.py
│   ├── mol.py
│   └── reaction_utils.py
├── tests/             # Tests unitaires
├── pyproject.toml     # Configuration du projet & système de build
└── README.md          # Documentation
```

## 👤 Autrice
Elisa Kaing