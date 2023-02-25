"""
Diminui regiões escuras da imagem
Aumenta regiões claras da imagem
"""
import cv2 as cv
import numpy as np

img = cv.imread('imagem2.png')  # Entrada da Imagem

kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))

dst = cv.dilate(img, kernel, iterations=1)
imgs_concat = np.concatenate((img, dst), axis=1)  # Concatena as imagens para ficar uma ao lado da outra

cv.imshow('resultado', imgs_concat)  # Apresenta as imagens
cv.waitKey(0)  # Espera para a janela ser fechada
cv.destroyAllWindows()
