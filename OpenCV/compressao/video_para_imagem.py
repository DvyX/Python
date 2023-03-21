"""
Converte um video em imagens, separando cada frame
"""
import cv2 as cv

vidcap = cv.VideoCapture('video1.mp4')  # Ler o video
success, frame = vidcap.read()
count = 0

while success:
    cv.imwrite('Frames\\frame%d.jpg' % count, frame)
    success, image = vidcap.read()
    print('Ler novo frame: ', success)
    count += 1
