"""
Pega cada frame e transforma em um video
"""
import cv2 as cv
import numpy as np
import glob

img_array = []

for filename in glob.glob('Frames/*.jpg'):  # Seleciona todos as imagens/frames
    img = cv.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)  # Adiciona todas as imagens/frames no array

dst = cv.VideoWriter('v.avi', cv.VideoWriter_fourcc(*'FMP4'), 24, size)

for i in range(len(img_array)):
    dst.write(img_array[i])
dst.release()
