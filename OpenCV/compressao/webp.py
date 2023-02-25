"""
Formato BMP é pesado, convertendo ele para WebP otimiza a imagem
- Pode chegar a número incrívelmente baixos quando otimizado, porém não é muito conveniente de ser utilizado
"""
import cv2 as cv
import numpy as np
import os

img = cv.imread("imagem4.bmp")
print("Kb of Img1 BMP =", int(os.path.getsize("imagem4.bmp") / 1024))  # Mostra o tamanho da imagem BMP

modo = 2  # modo 1 para imagem com 100% de qualidade, outro modo para imagem com menos qualidade
if modo == 1:
    cv.imwrite('imagem4_Comp_WebP.webp', img, [int(cv.IMWRITE_WEBP_QUALITY), 100])  # Escreve uma nova imagem
    # Seleciona 'img', converte em WebP com qualidade 100%
else:
    cv.imwrite('imagem4_Comp_WebP.webp', img, [int(cv.IMWRITE_WEBP_QUALITY), 5])  # Escreve uma nova imagem
    # Seleciona 'img', converte em WebP com qualidade 5%

dst = cv.imread("imagem4_Comp_WebP.webp")
print("Kb of Img2 WebP =", int(os.path.getsize("imagem4_Comp_WebP.webp") / 1024))  # Mostra o tamanho da imagem WebP

imgs_concat = np.concatenate((img, dst), axis=1)  # Concatena as imagens para ficar uma ao lado da outra

cv.imshow('resultado', imgs_concat)  # Apresenta as imagens
cv.waitKey(0)  # Espera para a janela ser fechada
cv.destroyAllWindows()
