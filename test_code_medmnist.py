import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def extract_and_organize(local_npz_path, output_path, class_names):
    # Load the dataset from the local .npz file
    data = np.load(local_npz_path)

    # Extract images and labels for training, validation, and test sets
    train_images = data['train_images']
    train_labels = data['train_labels']
    val_images = data['val_images']
    val_labels = data['val_labels']
    test_images = data['test_images']
    test_labels = data['test_labels']

    # Function to create directories and save images
    def save_images(images, labels, split_name):
        split_dir = os.path.join(output_path, split_name)
        os.makedirs(split_dir, exist_ok=True)
        for class_idx, class_name in enumerate(class_names):
            class_dir = os.path.join(split_dir, class_name)
            os.makedirs(class_dir, exist_ok=True)

        for idx, (img, label) in enumerate(zip(images, labels)):
            class_dir = os.path.join(split_dir, class_names[label[0]])
            img_path = os.path.join(class_dir, f"{idx}.png")
            img = Image.fromarray(img.squeeze())  # Ensure the image is 2D
            img.save(img_path)

    # Create root directory
    os.makedirs(output_path, exist_ok=True)

    # Save images for each split
    save_images(train_images, train_labels, 'train')
    save_images(val_images, val_labels, 'val')
    save_images(test_images, test_labels, 'test')

    print(f'Images extracted and organized into {output_path}.')

if __name__ == "__main__":
    # Path to your local .npz file
    local_npz_path = '/Users/hanadabdullahi/Downloads/pneumoniamnist_224.npz'  # Replace with your file path
    # Path to save the organized dataset
    output_path = '/Users/hanadabdullahi/Downloads/organized_pneumoniamnist'  # Replace with your desired output path
    
    extract_and_organize(local_npz_path, output_path, ['Normal', 'Pneumonia'])

# Function to plot images with class names
def plot_images(images, labels, class_names, num=10):
    plt.figure(figsize=(10, 10))
    for i in range(num):
        plt.subplot(1, num, i + 1)
        plt.imshow(images[i], cmap='gray')
        plt.title(class_names[labels[i][0]])
        plt.axis('off')
    plt.show()

# Load the data again to plot
data = np.load('/Users/hanadabdullahi/Downloads/pneumoniamnist_224.npz')
train_images = data['train_images']
train_labels = data['train_labels']

# Display the first 10 images and their labels from the training set
plot_images(train_images, train_labels, ['Normal', 'Pneumonia'])
