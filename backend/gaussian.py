import cv2

image = cv2.imread(
    r'f:\SideProject\computer-vision_playground\backend\uploads\arch.png')
blurred_image = cv2.GaussianBlur(image, (19, 19), 0)
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
