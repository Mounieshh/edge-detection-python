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
    # Initialize camera
    camera = cv.VideoCapture(0)

    while True:
        ret, frame = camera.read()

        if not ret:
            print("Error: Unable to capture frame.")
            break

        cv.imshow('Original', frame)

        # Apply Laplacian edge detection
        laplacian = laplacian_edge_detection(frame)
        cv.imshow('Laplacian Edges', laplacian)

        # Apply Canny edge detection
        edges = canny_edge_detection(frame)
        cv.imshow('Canny Edges', edges)

        # Break the loop if 'x' is pressed
        if cv.waitKey(1) & 0xFF == ord('x'):
            break

    camera.release()
    cv.destroyAllWindows()

# Call the main function
if __name__ == "__main__":
    main()
