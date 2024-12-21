"""
Name:  Kevin Fang
File: image_utils.py
Description: 
    This file is responsible for utility function related to image loading,
    saving, displaying (display function wasn't used in the current main.py),
    adding Gaussian blur and noise to the input images.
    
    The file and its functions are also meant to be imported into the main.py file
    through the line in the main.py:
    from image_utils import load_image, display_image, save_image, apply_gaussian_blur, add_gaussian_noise
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"Image not found at path: {image_path}")
    return image

def display_image(image, title="Image"):
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()
    
def save_image(image, output_path):
    cv2.imwrite(output_path, image)
    print(f"Image saved at: {output_path}")

def apply_gaussian_blur(image, kernel_size=(15, 15), sigma=5):
    return cv2.GaussianBlur(image, kernel_size, sigma)

def add_gaussian_noise(image, mean=0, std_dev=20):
    noise = np.random.normal(mean, std_dev, image.shape).astype(np.float32)
    noisy_image = cv2.add(image.astype(np.float32), noise)
    return np.clip(noisy_image, 0, 255).astype(np.uint8)