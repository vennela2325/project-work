import cv2
import numpy as np

# Load the original image and watermark image
original_img = cv2.imread('original_img.png', cv2.IMREAD_GRAYSCALE)
watermark_img = cv2.imread('watermark_img.png', cv2.IMREAD_GRAYSCALE)

# Get the dimensions of the watermark image
watermark_height, watermark_width = watermark_img.shape[:2]

# Select a region of interest (RI) in the original image to embed the watermark
# Here, we select the top-left corner of the original image as the RI
ri_top_left = (0, 0)
ri_bottom_right = (watermark_width, watermark_height)

# Resize the watermark image to match the RI size
watermark_img = cv2.resize(watermark_img, (ri_bottom_right[0], ri_bottom_right[1]))

# Get the updated dimensions
watermark_height, watermark_width = watermark_img.shape[:2]

ri = original_img[ri_top_left[1]:ri_bottom_right[1], ri_top_left[0]:ri_bottom_right[0]]

# Sort the pixels in the RI by their intensity values
sorted_pixels = np.sort(ri.flatten())

# Embed the watermark image into the RI using the LSB technique
for i in range(watermark_height):
    for j in range(watermark_width):
        # Get the current pixel value in the RI
        curr_pixel = ri[i, j]

        # Get the corresponding pixel value in the sorted list of pixels
        sorted_pixel_idx = np.where(sorted_pixels == curr_pixel)[0][0]

        # Get the watermark bit to embed at this pixel location
        watermark_bit = (watermark_img[i, j] & 1)

        # Embed the watermark bit into the LSB of the current pixel value
        new_pixel = (curr_pixel & ~1) | watermark_bit

        # Update the pixel value in the RI
        ri[i, j] = new_pixel

# Save the watermarked image
cv2.imwrite('watermarked_img.png', original_img)
