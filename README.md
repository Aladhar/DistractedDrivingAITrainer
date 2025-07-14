# Distracted Driver Detection Project

## Overview
This project focuses on building and training neural networks to classify distracted driver behavior using real-world image data. We explore different deep learning techniques, including basic neural networks (MLPs), Convolutional Neural Networks (CNNs), and Transfer Learning with VGG16 to improve accuracy and generalization.

## Technologies Used
- Python, TensorFlow, Keras, NumPy, Pandas, Matplotlib, Seaborn
- Jupyter Notebooks, Google Colab

## Project Structure
<see folder layout in repo>

## Model Performance Summary
| Model              | Train Accuracy | Validation Accuracy | Notes                 |
|-------------------|----------------|----------------------|-----------------------|
| MLP (2-layer)     | ~97%           | ~32%                 | Overfitting observed  |
| CNN (3-layer)     | ~96%           | ~39%                 | Improved generalization |
| VGG16 (Transfer)  | ~98%           | ~80–85%              | Best model accuracy   |

## Getting Started
1. Place `image_data.npy` and `metadata.csv` in the `data/` folder
2. Run each notebook in sequence from `notebooks/`
3. Use `plot_acc()` to visualize training results
4. Load `model.h5` from `model_weights/` if desired

## Author
GitHub: [github.com/ALadhar](https://github.com/ALadhar)
