import cv2 as cv
import numpy as np

def sobel_edge_detection(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0, ksize=5)
    sobely = cv.Sobel(gray, cv.CV_64F, 0, 1, ksize=5)
    sobel = np.hypot(sobelx, sobely)
    sobel = np.uint8(sobel / np.max(sobel) * 255)
    return sobel

def laplacian_edge_detection(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    laplacian = cv.Laplacian(gray, cv.CV_64F)
    laplacian = np.uint8(np.absolute(laplacian))
    return laplacian

def canny_edge_detection(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 80, 120)
    return edges

def combine_edge_detections(image):
    sobel = sobel_edge_detection(image)
    laplacian = laplacian_edge_detection(image)
    canny = canny_edge_detection(image)
    
    combined_edges = np.maximum(np.maximum(sobel, laplacian), canny)
    return combined_edges

def main():
    # Initialize camera
    camera = cv.VideoCapture(0)

    while True:
        ret, frame = camera.read()

        if not ret:
            print("Error: Unable to capture frame.")
            break

        cv.imshow('Original', frame)

        # Combine edges from multiple algorithms
        combined_edges = combine_edge_detections(frame)
        cv.imshow('Combined Edges', combined_edges)

        # Break the loop if 'x' is pressed
        if cv.waitKey(1) & 0xFF == ord('x'):
            break

    camera.release()
    cv.destroyAllWindows()

# Call the main function
if __name__ == "__main__":
    main()
