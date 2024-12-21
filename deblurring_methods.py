"""
Name:  Kevin Fang
File: deblurring_methods.py
Description: 
    This file is responsible for the deblurring algorithms (Wiener filter and Lucy-Richardson)
    that were meant to reduce the effects of noise and blur in the altered images.
    It is also responsible for calculating the metric scores (PSNR, SSIM) of the newly
    deblurred images to the original images. 
    
    The file and its functions are also meant to be imported into the main.py file
    through the line in the main.py:
    from deblurring_methods import apply_wiener_filter, apply_lucy_richardson, calculate_psnr, calculate_ssim

"""
import cv2
import numpy as np
from skimage.restoration import wiener, richardson_lucy
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import structural_similarity as ssim

def apply_wiener_filter(noisy_image, kernel_size=5):
    normalized_image = noisy_image / 255.0
    kernel = np.ones((kernel_size, kernel_size)) / (kernel_size ** 2)
    
    filtered_image = cv2.filter2D(normalized_image, -1, kernel)
    noise_variance = np.var(normalized_image - filtered_image)
    
    # Applying the Wiener filter
    deblurred_image = wiener(normalized_image, kernel, noise_variance)
    
    # Scale the result back to [0, 255] and convert to uint8
    return np.clip(deblurred_image * 255, 0, 255).astype(np.uint8)

def apply_lucy_richardson(noisy_image, psf, iterations=30):
    noisy_image_normalized = noisy_image / 255.0
    
    # Performing Lucy-Richardson deconvolution
    deblurred_image = richardson_lucy(noisy_image_normalized, psf, num_iter=iterations)
    deblurred_image = np.clip(deblurred_image * 255, 0, 255).astype(np.uint8)
    return deblurred_image

def calculate_psnr(original_image, processed_image):
    """
    Calculate PSNR between the original and processed images.
    """
    return psnr(original_image, processed_image, data_range=255)

def calculate_ssim(original_image, processed_image):
    """
    Calculate SSIM between the original and processed images.
    """
    return ssim(original_image, processed_image, data_range=255)