i. Completed Parts:
    image_utils.py deblurring_methods.py main.py

ii. Bugs and Errors:
    None

iii. How to run program:
    Make sure to have all libraries installed
    python main.py

iv. Input and Output Files:
    image_utils.py
    deblurring_methods.py
    main.py
    input_image1.jpeg (used as input in main.py)
    input_image2.jpg (used as input in main.py)

    Outputs for input_image1.jpeg:
        Directory/folder called output_images_1, containing:
            original_image1.jpg
            blurred_image.jpg
            noisy_image.jpg
            noisy_wiener_deblurred.jpg
            blurry_wiener_deblurred.jpg
            noisy_lucy_deblurred.jpg
            blurry_lucy_deblurred.jpg

    Outputs for input_image2.jpg: 
        Directory/folder called output_images_2, containing:
            original_image2.jpg
            blurred_image2.jpg
            noisy_image2.jpg
            noisy_wiener_deblurred2.jpg
            blurry_wiener_deblurred2.jpg
            noisy_lucy_deblurred2.jpg
            blurry_lucy_deblurred2.jpg

    For metric results, it should appear in the terminal, which should look like for each input image:
    input_image1.jpeg:
        These are the metric scores for the blurry-noisy images
        PSNR (Wiener Filter): 18.23
        PSNR (Lucy-Richardson): 23.27
        SSIM (Wiener Filter): 0.08
        SSIM (Lucy-Richardson): 0.45

        These are the metric scores for the blurry-only images
        PSNR (Wiener Filter): 19.23
        PSNR (Lucy-Richardson): 25.02
        SSIM (Wiener Filter): 0.19
        SSIM (Lucy-Richardson): 0.81

    input_image2.jpg:
        These are the metric scores for the blurry-noisy images
        PSNR (Wiener Filter): 15.61
        PSNR (Lucy-Richardson): 16.57
        SSIM (Wiener Filter): 0.12
        SSIM (Lucy-Richardson): 0.34

        These are the metric scores for the blurry-only images
        PSNR (Wiener Filter): 16.01
        PSNR (Lucy-Richardson): 16.90
        SSIM (Wiener Filter): 0.20
        SSIM (Lucy-Richardson): 0.43