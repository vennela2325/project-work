import cv2
import numpy as np

# Load the watermarked image and select the region of interest (RI) used for watermark embedding
watermarked_img = cv2.imread('watermarked_img.png', cv2.IMREAD_GRAYSCALE)
watermark_height, watermark_width = 100, 100
ri_top_left = (0, 0)
ri_bottom_right = (watermark_width, watermark_height)
ri = watermarked_img[ri_top_left[1]:ri_bottom_right[1], ri_top_left[0]:ri_bottom_right[0]]

# Extract the watermark by iterating over each pixel in the RI and extracting its LSB
watermark = np.zeros((watermark_height, watermark_width), dtype=np.uint8)
for i in range(watermark_height):
    for j in range(watermark_width):
        watermark[i, j] = ri[i, j] & 1

# Display the extracted watermark
cv2.imshow('Extracted watermark', watermark * 255)
cv2.waitKey(0)
cv2.destroyAllWindows()
