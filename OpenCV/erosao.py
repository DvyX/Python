"""
Diminui regiões claras da imagem
Aumenta regiões escuras da imagem
"""
import cv2 as cv
import numpy as np

img = cv.imread('imagem3.png', 0)  # Entrada da Imagem

kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))

dst = cv.erode(img, kernel, iterations=1)
imgs_concat = np.concatenate((img, dst), axis=1)  # Concatena as imagens para ficar uma ao lado da outra

cv.imshow('resultado', imgs_concat)  # Apresenta as imagens
cv.waitKey(0)  # Espera para a janela ser fechada
cv.destroyAllWindows()
