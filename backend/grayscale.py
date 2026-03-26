import cv2


def gray(path):
    image = cv2.imread(path, 0)
    if image is None:
        raise FileNotFoundError(f"Could not load image: {path}")

    output_path = path.replace(".", "_grayscaled_image.")
    cv2.imwrite(output_path, image)

    # cv2.imshow('Image', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return output_path


# print(gray(r'uploads\castle.png'))
