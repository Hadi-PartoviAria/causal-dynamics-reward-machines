import os
import torch
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


model_dir = "rslts/dynamics/<your_run>/trained_models"  # path to your trained dynamics model

def load_inference_data(model_dir):
    for filename in os.listdir(model_dir):
        if 'inference' in filename:
            data_path = os.path.join(model_dir, filename)
            return torch.load(data_path, map_location=torch.device("cpu"))
    raise ValueError("Inference data not found in provided directory!")

def extract_adjacency_matrix(inference_data):

    return inference_data['mask_CMI'].detach().numpy() * 100

def plot_adjacency_matrix(matrix):
    plt.figure(figsize=(10, 10))
    sns.heatmap(matrix, linewidths=1, square=True, annot=True, cbar=False)
    plt.title('Adjacency Matrix')
    plt.show()

if __name__ == "__main__":
    inference_data = load_inference_data(model_dir)
    print(f"Number of items in inference_data: {len(inference_data)}")
    
    adjacency_matrix = extract_adjacency_matrix(inference_data)
    
    plot_adjacency_matrix(adjacency_matrix)




    
