"""
Name:  Kevin Fang
File: main.py
Description: 
    Coordinates the image deblurring process/workflow
"""
import os
import cv2
from image_utils import load_image, display_image, save_image, apply_gaussian_blur, add_gaussian_noise
from deblurring_methods import apply_wiener_filter, apply_lucy_richardson, calculate_psnr, calculate_ssim

def main():
    # Paths for input and output images
    input_image_path = "input_image1.jpeg"  # Replace with your image path
    output_dir = "output_images_1"
    
    # Creating the directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Step 1: Load the image
    try:
        original_image = load_image(input_image_path)
        save_image(original_image, os.path.join(output_dir, "original_image1.jpg"))
    except FileNotFoundError as error:
        print(error)
        return
    
    # Step 2: Apply Gaussian blur
    blurred_image = apply_gaussian_blur(original_image, kernel_size=(15, 15), sigma=5)
    save_image(blurred_image, os.path.join(output_dir, "blurred_image.jpg"))
    
    # Step 3: Add Gaussian noise
    noisy_image = add_gaussian_noise(blurred_image, mean=0, std_dev=20)
    save_image(noisy_image, os.path.join(output_dir, "noisy_image.jpg"))
    
    # Step 4: Apply Wiener filtering
    # Noisy route
    noisy_wiener_deblurred = apply_wiener_filter(noisy_image, kernel_size=5)
    save_image(noisy_wiener_deblurred, os.path.join(output_dir, "noisy_wiener_deblurred.jpg"))
    
    # Blurry
    blurry_wiener_deblurred = apply_wiener_filter(blurred_image, kernel_size=5)
    save_image(blurry_wiener_deblurred, os.path.join(output_dir, "blurry_wiener_deblurred.jpg"))
    
    # Step 5: Apply Lucy-Richardson deconvolution
    psf = cv2.getGaussianKernel(15, 5)  # Create a Gaussian PSF matching the blur
    psf = psf @ psf.T  # Convert 1D kernel to 2D

    # Noisy
    noisy_lucy_deblurred = apply_lucy_richardson(noisy_image, psf, iterations=30)
    save_image(noisy_lucy_deblurred, os.path.join(output_dir, "noisy_lucy_deblurred.jpg"))
    
    # Blurry
    blurry_lucy_deblurred = apply_lucy_richardson(blurred_image, psf, iterations=30)
    save_image(blurry_lucy_deblurred, os.path.join(output_dir, "blurry_lucy_deblurred.jpg"))
    
    # Step 6: Compare the results using PSNR and SSIM
    # Noisy images
    psnr_wiener = calculate_psnr(original_image, noisy_wiener_deblurred)
    psnr_lucy = calculate_psnr(original_image, noisy_lucy_deblurred)
    
    ssim_wiener = calculate_ssim(original_image, noisy_wiener_deblurred)
    ssim_lucy = calculate_ssim(original_image, noisy_lucy_deblurred)
    
    # With blurred images only (not noisy)
    psnr_wiener2 = calculate_psnr(original_image, blurry_wiener_deblurred)
    psnr_lucy2 = calculate_psnr(original_image, blurry_lucy_deblurred)
    
    ssim_wiener2 = calculate_ssim(original_image, blurry_wiener_deblurred)
    ssim_lucy2 = calculate_ssim(original_image, blurry_lucy_deblurred)
    
    # Printing metric scores of the noisy route
    print("\nThese are the metric scores for the blurry-noisy images")
    print(f"PSNR (Wiener Filter): {psnr_wiener:.2f}")
    print(f"PSNR (Lucy-Richardson): {psnr_lucy:.2f}")
    print(f"SSIM (Wiener Filter): {ssim_wiener:.2f}")
    print(f"SSIM (Lucy-Richardson): {ssim_lucy:.2f}")
    
    # Printing metric scores of the blurry route
    print("\nThese are the metric scores for the blurry-only images")
    print(f"PSNR (Wiener Filter): {psnr_wiener2:.2f}")
    print(f"PSNR (Lucy-Richardson): {psnr_lucy2:.2f}")
    print(f"SSIM (Wiener Filter): {ssim_wiener2:.2f}")
    print(f"SSIM (Lucy-Richardson): {ssim_lucy2:.2f}")

def main_two():
    print("\n\nThis next section is for the second image\n")
    # Paths for input and output images
    input_image_path = "input_image2.jpg"  # Replace with your image path
    output_dir = "output_images_2"
    
    # Create the directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Step 1: Load the image
    try:
        original_image = load_image(input_image_path)
        save_image(original_image, os.path.join(output_dir, "original_image2.jpg"))
    except FileNotFoundError as error:
        print(error)
        return
    
    # Step 2: Apply Gaussian blur
    blurred_image = apply_gaussian_blur(original_image, kernel_size=(15, 15), sigma=5)
    save_image(blurred_image, os.path.join(output_dir, "blurred_image2.jpg"))
    
    # Step 3: Add Gaussian noise
    noisy_image = add_gaussian_noise(blurred_image, mean=0, std_dev=20)
    save_image(noisy_image, os.path.join(output_dir, "noisy_image2.jpg"))
    
    # Step 4: Apply Wiener filtering
    # Noisy route
    noisy_wiener_deblurred = apply_wiener_filter(noisy_image, kernel_size=5)
    save_image(noisy_wiener_deblurred, os.path.join(output_dir, "noisy_wiener_deblurred2.jpg"))
    
    # Blurry
    blurry_wiener_deblurred = apply_wiener_filter(blurred_image, kernel_size=5)
    save_image(blurry_wiener_deblurred, os.path.join(output_dir, "blurry_wiener_deblurred2.jpg"))
    
    # Step 5: Apply Lucy-Richardson deconvolution
    psf = cv2.getGaussianKernel(15, 5)  # Create a Gaussian PSF matching the blur
    psf = psf @ psf.T  # Convert 1D kernel to 2D

    # Noisy
    noisy_lucy_deblurred = apply_lucy_richardson(noisy_image, psf, iterations=30)
    save_image(noisy_lucy_deblurred, os.path.join(output_dir, "noisy_lucy_deblurred2.jpg"))
    
    # Blurry
    blurry_lucy_deblurred = apply_lucy_richardson(blurred_image, psf, iterations=30)
    save_image(blurry_lucy_deblurred, os.path.join(output_dir, "blurry_lucy_deblurred2.jpg"))
    
    # Step 6: Compare the results using PSNR and SSIM
    # Noisy images
    psnr_wiener = calculate_psnr(original_image, noisy_wiener_deblurred)
    psnr_lucy = calculate_psnr(original_image, noisy_lucy_deblurred)
    
    ssim_wiener = calculate_ssim(original_image, noisy_wiener_deblurred)
    ssim_lucy = calculate_ssim(original_image, noisy_lucy_deblurred)
    
    # With blurred images only (not noisy)
    psnr_wiener2 = calculate_psnr(original_image, blurry_wiener_deblurred)
    psnr_lucy2 = calculate_psnr(original_image, blurry_lucy_deblurred)
    
    ssim_wiener2 = calculate_ssim(original_image, blurry_wiener_deblurred)
    ssim_lucy2 = calculate_ssim(original_image, blurry_lucy_deblurred)
    
    # Printing metric scores of the noisy route
    print("\nThese are the metric scores for the blurry-noisy images")
    print(f"PSNR (Wiener Filter): {psnr_wiener:.2f}")
    print(f"PSNR (Lucy-Richardson): {psnr_lucy:.2f}")
    print(f"SSIM (Wiener Filter): {ssim_wiener:.2f}")
    print(f"SSIM (Lucy-Richardson): {ssim_lucy:.2f}")
    
    # Printing metric scores of the blurry route
    print("\nThese are the metric scores for the blurry-only images")
    print(f"PSNR (Wiener Filter): {psnr_wiener2:.2f}")
    print(f"PSNR (Lucy-Richardson): {psnr_lucy2:.2f}")
    print(f"SSIM (Wiener Filter): {ssim_wiener2:.2f}")
    print(f"SSIM (Lucy-Richardson): {ssim_lucy2:.2f}")

    
if __name__ == "__main__":
    main()
    main_two()