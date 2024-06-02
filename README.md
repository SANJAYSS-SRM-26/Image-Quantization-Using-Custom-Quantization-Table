# Image Quantization Using Custom Quantization Table

## Project Description

This project demonstrates the process of image quantization using a custom quantization table. <br>
The image quantization reduces the number of distinct gray levels in an image, which can be useful for image compression and other applications.<br> 
In this project, a grayscale image is loaded, quantized using predefined ranges and values, and the results are visualized using histograms.

## Files in the Repository

- **quantization.py**: The main script that performs the image quantization and plots histograms.
- **Picture2.jpg**: The input grayscale image to be quantized.
- **reconstructed_image.jpg**: The output quantized image.

## Steps to Run the Code

1. **Install Required Libraries**:
   
   Ensure you have the necessary Python libraries installed. You can install them using pip:
   ```bash
   pip install numpy opencv-python matplotlib
   ```
2. **Run the Script**:
   
    Execute the image_quantization.py script to perform the quantization and visualize the results:
   ```bash
   python image_quantization.py
   ```

Check Output:

The script will generate and save a quantized version of the input image (reconstructed_image.jpg) and display histograms comparing the original and quantized images.

## Visualization

The script plots two histograms:
Histogram of the original image pixel values.
Histogram of the quantized image pixel values.

## Acknowledgments

This project utilizes the OpenCV library for image processing and Matplotlib for visualization.
