import numpy as np
import cv2
import matplotlib.pyplot as plt

image_path = "D:\DIP impathon\Picture2.jpg" 
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    raise FileNotFoundError("Could not read the image. Please check the image path.")

quantization_table = {
    (0, 16): 7,
    (17, 31): 23,
    (32, 47): 39,
    (48, 63): 55,
    (64, 79): 71,
    (80, 95): 87,
    (96, 111): 102,
    (112, 127): 120,
    (128, 143): 135,
    (144, 158): 150,
    (159, 175): 165,
    (176, 192): 185,
    (193, 207): 199,
    (208, 223): 215,
    (224, 240): 232,
    (241, 255): 250
}

quantized_image = np.zeros_like(image)
for key, value in quantization_table.items():
    quantized_image[(image >= key[0]) & (image <= key[1])] = value

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.hist(image.flatten(), bins=256, range=(0, 255), color='b')
plt.title('Histogram of Original Image')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(quantized_image.flatten(), bins=256, range=(0, 255), color='r')
plt.title('Histogram of Quantized Image')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

cv2.imwrite("reconstructed_image.jpg", quantized_image)

plt.show()
