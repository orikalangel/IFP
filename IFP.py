import cv2
import numpy as np

def compare_focus(image1_path, image2_path):
    # Load the images
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    # Convert images to grayscale
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Calculate the Laplacian variance as a measure of focus
    focus1 = cv2.Laplacian(gray1, cv2.CV_64F).var()
    focus2 = cv2.Laplacian(gray2, cv2.CV_64F).var()

    # Calculate the focus percentage for each image
    total_pixels = gray1.shape[0] * gray1.shape[1]
    focus_percentage1 = (focus1 / total_pixels) * 100
    focus_percentage2 = (focus2 / total_pixels) * 100

    return focus_percentage1, focus_percentage2
image1_path = 'path/to/image1.jpg'
image2_path = 'path/to/image2.jpg'
focus_percentage1, focus_percentage2 = compare_focus(image1_path, image2_path)
print(f"Focus percentage for image1: {focus_percentage1}%")
print(f"Focus percentage for image2: {focus_percentage2}%")