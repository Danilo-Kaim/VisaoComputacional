# -*- coding: utf-8 -*-
"""gamma.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Pd_NDsfgmK_h2-OHq1TaeJcFWN2qp4o5
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import FloatSlider, interact

def gamma_correction_LUT(img, gamma, c=1.0):
    # Cria uma Lookup Table (LUT)
    GAMMA_LUT = np.array([c * ((i / 255.0) ** (1.0 / gamma)) * 255 for i in np.arange(0, 256)]).astype("uint8")

    # Aplica a transformação usando LUT
    return cv2.LUT(img, GAMMA_LUT)

def update_image(gamma):
    im_gamma = gamma_correction_LUT(im, gamma)
    plt.imshow(cv2.cvtColor(im_gamma, cv2.COLOR_BGR2RGB))
    plt.axis('off')  # Não mostra eixos
    plt.show()  # Atualiza a imagem exibida

# Abre imagem
filename = '/content/jato.jpg'
im = cv2.imread(filename)

# Inicializa a figura do Matplotlib
plt.figure('image')

# Exibe a imagem original inicialmente
plt.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
plt.axis('off')  # Não mostra eixos
plt.show()

# Cria um slider para ajustar gamma
gamma_slider = FloatSlider(value=1.0, min=0.1, max=10, step=0.01, description='Gamma:')
interact(update_image, gamma=gamma_slider)

