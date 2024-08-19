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
    # Load three input images
    input_image1 = cv.imread('pexels-kubrakuzu-20068318 (1).jpg')
    input_image2 = cv.imread('pexels-justinianoadriano-1864189.jpg')
    input_image3 = cv.imread('jellyfish-7340188_1280.jpg')

    # Check if the images are loaded successfully
    if input_image1 is None or input_image2 is None or input_image3 is None:
        print("Error: Unable to load one or more images.")
        return

    # Display original images
    cv.imshow('Original Image 1', input_image1)
    cv.imshow('Original Image 2', input_image2)
    cv.imshow('Original Image 3', input_image3)

    # Apply Laplacian edge detection to each image
    laplacian1 = laplacian_edge_detection(input_image1)
    laplacian2 = laplacian_edge_detection(input_image2)
    laplacian3 = laplacian_edge_detection(input_image3)

    # Display Laplacian edges
    cv.imshow('Laplacian Edges 1', laplacian1)
    cv.imshow('Laplacian Edges 2', laplacian2)
    cv.imshow('Laplacian Edges 3', laplacian3)

    # Apply Canny edge detection to each image
    edges1 = canny_edge_detection(input_image1)
    edges2 = canny_edge_detection(input_image2)
    edges3 = canny_edge_detection(input_image3)

    # Display Canny edges
    cv.imshow('Canny Edges 1', edges1)
    cv.imshow('Canny Edges 2', edges2)
    cv.imshow('Canny Edges 3', edges3)

    # Wait for a key press and close OpenCV windows
    cv.waitKey(0)
    cv.destroyAllWindows()

# Call the main function
if __name__ == "__main__":
    main()
