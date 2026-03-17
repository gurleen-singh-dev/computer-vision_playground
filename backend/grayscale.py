import cv2

image = cv2.imread(
    r'f:\SideProject\computer-vision_playground\backend\uploads\arch.png', 0)

if image is None:
    print("Error: Could not read the image file")
else:
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()