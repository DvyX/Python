import cv2 as cv
import numpy as np

img = cv.imread('../imagem1.png')  # Entrada da Imagem

blur1 = cv.blur(img, (3, 3))  # Níveis de blur da imagem
blur2 = cv.blur(blur1, (3, 3))
blur3 = cv.blur(blur2, (3, 3))

imgs_concat = np.concatenate((img, blur1, blur2, blur3), axis=1)  # Concatena as imagens para ficar uma ao lado da outra

cv.imshow('resultado', imgs_concat)  # Apresenta as imagens
cv.waitKey(0)  # Espera para a janela ser fechada
cv.destroyAllWindows()