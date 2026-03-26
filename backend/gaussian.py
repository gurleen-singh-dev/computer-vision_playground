import cv2


def gaussian(path):
    image = cv2.imread(path)
    if image is None:
        raise FileNotFoundError(f"Could not load image: {path}")

    blurred_image = cv2.GaussianBlur(image, (19, 19), 0)
    output_path = path.replace(".", "_blurred_image.")
    cv2.imwrite(output_path, blurred_image)
    # cv2.imshow('Original Image', image)
    # cv2.imshow('Blurred Image', blurred_image)
    # cv2.waitKey(0)

    return output_path


# print(gaussian(r"f:\SideProject\computer-vision_playground\uploads\arch.png"))
