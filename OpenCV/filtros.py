import time
import cv2 as cv
import numpy as np


def ler_imagem():
    img = cv.imread('imagem1.png')  # Entrada da Imagem
    return img


def menu():
    """
    Menu de escolhas de filtro
    :return: Número do filtro escolhido
    """
    try:
        while True:
            num = int(
                input('Escolha o filtro:\n1- Blur\n2- Gaussian\n3- Media\n4- Median Blur\n5- Prewitt\n6- Roberts\n7- '
                      'Sobel\n8- Laplacian\n'))
            if num not in range(1, 9):
                print('Número não registrado, tente novamente\n')
                time.sleep(2)
            else:
                break
        return num
    except ValueError:
        print('Erro: Valor digitado não é um número, tente novamente\n')
        time.sleep(2)
        menu()


def filtro(img, e):
    """
    Processamento de tipo de filtro
    :param img: Imagem original
    :param e: Número do filtro escolhido
    :return: Imagem editada
    """
    dst = None
    if e == 1:
        blur1 = cv.blur(img, (3, 3))
        blur2 = cv.blur(blur1, (3, 3))
        blur3 = cv.blur(blur2, (3, 3))
        dst = (blur1, blur2, blur3)
    elif e == 2:
        dst = cv.GaussianBlur(img, (5, 5), 0)
    elif e == 3:
        kernel = np.array([
            [1 / 5, 1 / 5, 1 / 5, 1 / 5, 1 / 5],
            [1 / 5, 1 / 5, 1 / 5, 1 / 5, 1 / 5],
            [1 / 5, 1 / 5, 1 / 5, 1 / 5, 1 / 5],
            [1 / 5, 1 / 5, 1 / 5, 1 / 5, 1 / 5],
            [1 / 5, 1 / 5, 1 / 5, 1 / 5, 1 / 5]
        ])
        dst = cv.filter2D(img, -1, kernel)
    elif e == 4:
        dst = cv.medianBlur(img, 5)
    elif e == 5:
        kernel = np.array([
            [-1, 0, 1],
            [-1, 0, 1],
            [-1, 0, 1]
        ])
        dst = cv.filter2D(img, -1, kernel)
    elif e == 6:
        kernel = np.array([
            [1, 0],
            [0, -1]
        ])
        dst = cv.filter2D(img, -1, kernel)
    elif e == 7:
        kernel = np.array([
            [1, 2, 1],
            [0, 0, 0],
            [-1, -2, -1]
        ])
        dst = cv.filter2D(img, -1, kernel)
    elif e == 8:
        kernel = np.array([
            [1, 1, 1],
            [1, -8, 1],
            [1, 1, 1]
        ])

        dst = cv.filter2D(img, -1, kernel)
    return dst


def contatenacao(img, e, dst):
    """
    Tipo de concatenação de imagem
    :param img: Imagem original
    :param dst: Imagem editada
    :param e: Número do filtro escolhido
    :return: Imagem concatenada
    """
    if e == 1:
        imgs_concat = np.concatenate((img, dst[0], dst[1], dst[2]), axis=1)
        return imgs_concat
    else:
        imgs_concat = np.concatenate((img, dst), axis=1)
        return imgs_concat


def apresentacao(img):
    cv.imshow('resultado', img)  # Apresenta as imagens
    print('Imagem Gerada')
    cv.waitKey(0)  # Espera para a janela ser fechada
    cv.destroyAllWindows()


def start():
    imagem = ler_imagem()
    escolha = menu()
    imagem_filtro = filtro(imagem, escolha) 
    resultado = contatenacao(imagem, escolha, imagem_filtro)
    apresentacao(resultado)


start()
