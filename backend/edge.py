import cv2


def edges(path, low_threshold=100, high_threshold=200):
    image = cv2.imread(path)
    if image is None:
        raise FileNotFoundError(f"Could not load image: {path}")

    edges = cv2.Canny(image, low_threshold, high_threshold)
    output_path = path.replace(".", "_edge_image.")
    cv2.imwrite(output_path, edges)

    # cv.imshow("Original", image)
    # cv.imshow("Edges", edges)
    # cv.waitKey(0)
    # cv.destroyAllWindows()
    return output_path


# print(edges(r'uploads\castle.png'))
