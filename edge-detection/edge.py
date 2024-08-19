import cv2 as cv
import numpy as np

def laplacian_edge_detection(image):
    # Convert the image to grayscale
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # Apply Laplacian edge detection
    laplacian = cv.Laplacian(gray, cv.CV_64F)
    laplacian = np.uint8(np.absolute(laplacian))
    return laplacian

def canny_edge_detection(image):
    # Apply Canny edge detection
    edges = cv.Canny(image, 80, 120)
    return edges

def main():

    input_image = cv.imread('pexels-kubrakuzu-20068318 (1).jpg')

    # Check if the image is loaded successfully
    if input_image is None:
        print("Error: Unable to load image.")
        return

    cv.imshow('Original', input_image)

    # Apply Laplacian edge detection
    laplacian = laplacian_edge_detection(input_image)
    cv.imshow('Laplacian Edges', laplacian)

    # Apply Canny edge detection
    edges = canny_edge_detection(input_image)
    cv.imshow('Canny Edges', edges)

    # Wait for a key press and close OpenCV windows
    cv.waitKey(0)
    cv.destroyAllWindows()

# Call the main function
if __name__ == "__main__":
    main()
