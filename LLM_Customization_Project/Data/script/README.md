# LLM Customization Project

Ce dépôt contient une architecture complète pour la personnalisation de grands modèles de langage (LLM) via le **fine-tuning supervisé**, le **pré-entrainement continué**, et le déploiement. Cette structure permet de gérer les données, les modèles, les scripts d’entraînement et de déploiement, ainsi que la documentation associée.

## Architecture du Projet

L'architecture de dossier est organisée comme suit :

- **Data/** : Contient les données utilisées pour le fine-tuning et le pré-entrainement continué.
  - `raw_data/` : Données brutes non traitées.
  - `processed_data/` : Données préparées pour l’entraînement.
  - `synthetic_data/` : Données synthétiques générées.

- **Models/** : Répertorie les modèles selon leur étape de personnalisation.
  - `base_models/` : Modèles de base, non personnalisés.
  - `fine_tuned_models/` : Modèles ayant subi le fine-tuning supervisé.
  - `continued_pretrained_models/` : Modèles ayant subi un pré-entrainement continué.
  - `compressed_models/` : Modèles optimisés pour le déploiement.

- **Training/** : Contient les scripts, configurations et checkpoints pour le processus de fine-tuning et de pré-entrainement.
  - `scripts/` : Scripts Python pour lancer les étapes d’entraînement.
  - `config/` : Fichiers de configuration pour les hyperparamètres.
  - `logs/` : Logs d’entraînement pour le suivi.
  - `checkpoints/` : Sauvegardes intermédiaires du modèle.

- **Evaluation/** : Gère les tests et rapports d'évaluation du modèle.
  - `test_data/` : Données de test pour l’évaluation.
  - `metrics/` : Scripts et fichiers pour calculer les métriques (précision, rappel, perplexité, etc.).
  - `human_evaluation/` : Résultats d’évaluations humaines si nécessaire.
  - `reports/` : Rapports d’évaluation finaux pour chaque version du modèle.

- **Deployment/** : Prépare le déploiement du modèle.
  - `docker/` : Fichiers Docker pour conteneuriser le modèle.
  - `kubernetes/` : Fichiers de configuration Kubernetes pour la mise à l’échelle.
  - `scaling/` : Scripts pour l'autoscaling.
  - `monitoring/` : Scripts pour le suivi en temps réel.

- **Documentation/** : Documentation complète du projet.
  - `methodology/` : Explication de la méthodologie de personnalisation.
  - `config_docs/` : Documentation des fichiers de configuration et hyperparamètres.
  - `evaluation_reports/` : Rapports d’évaluation pour chaque modèle.
  - `deployment_guide/` : Guide de déploiement.

## Instructions pour Créer l'Environnement de Travail

### Prérequis

Assurez-vous que **Make** est installé sur votre machine. Si ce n'est pas le cas, installez-le avec :

```bash
# Sur Ubuntu
sudo apt-get install make
