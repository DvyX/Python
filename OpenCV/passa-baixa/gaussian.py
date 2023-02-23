import cv2 as cv
import numpy as np

img = cv.imread('../imagem1.png')  # Entrada da Imagem
gauss = cv.GaussianBlur(img, (5, 5), 0)  # Aplica o filtro automático
imgs_concat = np.concatenate((img, gauss), axis=1)  # Concatena as imagens para ficar uma ao lado da outra

cv.imshow('resultado', imgs_concat)  # Apresenta as imagens
cv.waitKey(0)  # Espera para a janela ser fechada
cv.destroyAllWindows()