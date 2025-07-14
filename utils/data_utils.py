import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def label_to_numpy(labels):
    """
    Convert string labels to one-hot encoded NumPy arrays.
    Supports 4 classes: Attentive, DrinkingCoffee, UsingMirror, UsingRadio.
    """
    final_labels = np.zeros((len(labels), 4))
    label_map = {"Attentive": 0, "DrinkingCoffee": 1, "UsingMirror": 2, "UsingRadio": 3}
    for i, label in enumerate(labels):
        if label in label_map:
            final_labels[i, label_map[label]] = 1
    return final_labels

def plot_acc(history):
    """
    Plot training and validation accuracy over epochs from a Keras History object.
    Saves the plot as 'accuracy_plot.png' inside the plots directory.
    """
    history = history.history
    history.update({'epoch': list(range(len(history['val_accuracy'])))})
    history_df = pd.DataFrame.from_dict(history)
    best_epoch = history_df.sort_values(by='val_accuracy', ascending=False).iloc[0]['epoch']

    plt.figure(figsize=(10, 6))
    sns.lineplot(data=history_df, x='epoch', y='accuracy', label='Training')
    sns.lineplot(data=history_df, x='epoch', y='val_accuracy', label='Validation')
    plt.axhline(0.25, linestyle='--', color='red', label='Chance')
    plt.axvline(x=best_epoch, linestyle='--', color='green', label='Best Epoch')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.title('Training vs Validation Accuracy')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("plots/accuracy_plot.png")
    plt.close()
