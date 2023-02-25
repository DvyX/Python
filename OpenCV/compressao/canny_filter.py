"""
Devolve somente o contorno da imagem
"""
import cv2 as cv
import numpy as np

img = cv.imread('../imagem3.png')  # Entrada da Imagem

canny = cv.Canny(img, 10, 400)

dst = np.zeros_like(img)
dst[:, :, 0] = canny
dst[:, :, 1] = canny
dst[:, :, 2] = canny

imgs_concat = np.concatenate((img, dst), axis=1)  # Concatena as imagens para ficar uma ao lado da outra

cv.imshow('resultado', imgs_concat)  # Apresenta as imagens
cv.waitKey(0)  # Espera para a janela ser fechada
cv.destroyAllWindows()
