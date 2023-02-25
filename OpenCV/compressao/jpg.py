"""
Formato BMP é pesado, convertendo ele para JPG otimiza a imagem
- A queda de qualidade é muito brusca quanto mais se comprime
"""
import cv2 as cv
import numpy as np
import os

img = cv.imread("imagem4.bmp")
print("Kb of Img1 BMP =", int(os.path.getsize("imagem4.bmp") / 1024))  # Mostra o tamanho da imagem BMP

modo = 2  # modo 1 para imagem com 100% de qualidade, outro modo para imagem com menos qualidade
if modo == 1:
    cv.imwrite('imagem4_Comp_JPG.jpg', img, [int(cv.IMWRITE_JPEG_QUALITY), 100])  # Escreve uma nova imagem
    # Seleciona 'img', converte em JPG com qualidade 100%
else:
    cv.imwrite('imagem4_Comp_JPG.jpg', img, [int(cv.IMWRITE_JPEG_QUALITY), 5])  # Escreve uma nova imagem
    # Seleciona 'img', converte em JPG com qualidade 5%

dst = cv.imread("imagem4_Comp_JPG.jpg")
print("Kb of Img2 JPG =", int(os.path.getsize("imagem4_Comp_JPG.jpg") / 1024))  # Mostra o tamanho da imagem JPG

imgs_concat = np.concatenate((img, dst), axis=1)  # Concatena as imagens para ficar uma ao lado da outra

cv.imshow('resultado', imgs_concat)  # Apresenta as imagens
cv.waitKey(0)  # Espera para a janela ser fechada
cv.destroyAllWindows()
