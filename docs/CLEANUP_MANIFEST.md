# Cleanup Manifest

Original zip: `Colab Notebooks-20260428T180217Z-3-001.zip`

## Included files

- notebooks/01_breast_cancer_logistic_regression.ipynb
- notebooks/02_yelp_review_sentiment_classification.ipynb
- notebooks/03_conscientious_cars_knn_neural_networks.ipynb
- notebooks/04_conscientious_cars_cnn.ipynb
- notebooks/05_distracted_driver_data_exploration.ipynb
- notebooks/06_distracted_driver_neural_networks.ipynb
- notebooks/07_distracted_driver_saliency_and_evaluation.ipynb
- archive/yelp_review_sentiment_solution_reference.ipynb
- archive/rock_paper_scissors_teachable_machine.ipynb

## Removed duplicate

- `RockPaperScisors` — duplicate of the Rock Paper Scissors notebook, but missing the `.ipynb` extension and containing an extra blank code cell.

## Main cleanup decisions

- Kept the main project notebooks under `notebooks/`.
- Moved solution/reference/incomplete notebooks into `archive/`.
- Corrected the spelling and extension for Rock Paper Scissors.
- Updated the Rock Paper Scissors inference cell so it gives clearer missing-file errors instead of failing cryptically.
