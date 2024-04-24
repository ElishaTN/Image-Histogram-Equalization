import cv2
import numpy as np

def histogram_equalization(img):
    # Step 1: Calculating histogram
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    
    # Step 2: Calculating the cumulative histogram
    cdf = hist.cumsum()
    
    # Step 3: Masking all zeros (if any) in cdf to avoid divide-by-zero
    cdf_masked = np.ma.masked_equal(cdf, 0)
    
    # Step 4: Normalizing the histogram
    cdf_normalized = (cdf_masked - cdf_masked.min()) * 255 / (cdf_masked.max() - cdf_masked.min())
    
    # Converting masked elements back to 0
    cdf_normalized = np.ma.filled(cdf_normalized, 0).astype('uint8')
    
    # Step 5: Mapping the original image pixels to equalized value
    img_equalized = cdf_normalized[img]
    
    return img_equalized

# Loading an image in grayscale mode
img = cv2.imread('path_to_image.jpg', 0)  # Change 'path_to_image.jpg' to your image file path

# Applying the histogram equalization function
img_eq = histogram_equalization(img)

# Displaying the original and equalized images
cv2.imshow('Original Image', img)
cv2.imshow('Histogram Equalized Image', img_eq)
cv2.waitKey(0)
cv2.destroyAllWindows()
