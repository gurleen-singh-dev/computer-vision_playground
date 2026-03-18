import cv2 as cv
import sys


def detect_edges(image_path, low_threshold=100, high_threshold=200):
    image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"Could not load image: {image_path}")

    edges = cv.Canny(image, low_threshold, high_threshold)

    cv.imshow("Original (grayscale)", image)
    cv.imshow("Edges", edges)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    image_path = r'backend\uploads\arch.png'  # or 'uploads/arch.png'
    detect_edges(image_path)
