This project implements an Invisible Digital Watermarking technique ccusing the Least Significant Bit (LSB) technique. The goal is to embed a secret watermark inside an image in such a way that the watermark remains invisible to the human eye but can be extracted later for authentication and copyright protection.

The project is built in Python using OpenCV and NumPy, and was developed in PyCharm.
Features:

Embeds a watermark image invisibly inside a host image.

Uses LSB substitution for secure embedding.

Supports watermark extraction from the watermarked image.

Simple, lightweight, and easy to implement.

Demonstrates a fundamental image security and steganography approach.
Technique Used — LSB (Least Significant Bit):

The LSB of each pixel in the Region of Interest (ROI) of the original image is modified

The watermark bits are embedded into these least significant bits

This keeps visual quality intact while securely hiding the watermark.

Extraction retrieves the watermark by reading the LSBs back.

conclusion;
This project successfully demonstrates invisible watermark embedding using the LSB technique. The watermark is hidden without affecting the image's visual quality and can be accurately extracted later for verification. This method provides a simple, efficient approach for image authentication and copyright protection using basic image processing and Python tools.
