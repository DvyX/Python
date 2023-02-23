import cv2 as cv
import numpy as np

img = cv.imread('../imagem1.png')  # Entrada da Imagem

kernel = np.array([  # Imagem/Array manual de Auxilio para fazer o processamento do filtro
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
])

dst = cv.filter2D(img, -1, kernel)  # Processamento e imagem de destino manualmente
imgs_concat = np.concatenate((img, dst), axis=1)  # Concatena as imagens para ficar uma ao lado da outra

cv.imshow('resultado', imgs_concat)  # Apresenta as imagens
cv.waitKey(0)  # Espera para a janela ser fechada
cv.destroyAllWindows()