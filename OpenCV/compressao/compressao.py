import cv2 as cv
import numpy as np

img1 = cv.imread('../imagem3.png')
img1 = np.array(img1, dtype=np.uint16)
img1 *= 256
print(f"img1 = {img1.dtype}")

img2 = (img1/256).astype('uint8')
print(f"img2 = {img2.dtype}")

imgs_concat = np.concatenate((img1, img2), axis=1)

cv.imshow('resultado', imgs_concat)
cv.waitKey(0)
cv.destroyAllWindows()
