# Calculador de densidad de campo magnetico & corriente
# Para los calculos se parte del analisis de los circuitos magneticos los 
# cuales siguen normas similares a la leyes de Kirchoff para voltajes y
# corrientes.
# Ivan Rulik - Uniandes
# 22/04/19
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import sys
import os

from matplotlib.patches import Rectangle

from PIL import Image

os.system("cls")

#main
order = input('Manual data input? [Y/N]:')
if(order == 'Y'):
    #visual_guide
    posX1, posY1 = 0, 0
    plt.figure(1)
    currentAxis = plt.gca()
    currentAxis.add_patch(Rectangle((posX1 , posY1 ), 10, 60,color='blue'))
    currentAxis.add_patch(Rectangle((posX1 + 10, posY1 - 0), 32, 10,color='red'))
    currentAxis.add_patch(Rectangle((posX1 + 10, posY1 + 50), 32, 10,color='red'))
    currentAxis.add_patch(Rectangle((posX1 + 42, posY1 + 0), 2, 29,color='yellow'))
    currentAxis.add_patch(Rectangle((posX1 + 42, posY1 + 31), 2, 29,color='yellow'))
    plt.autoscale(enable=True, axis='both', tight=None)
    plt.title('Guide for the generator dimensions')
    plt.xlabel('example dim [mm]')
    plt.ylabel('example dim [mm]')
    plt.legend(['wc','w, da ',None,'g, wg',None])
    plt.show(block=False)
    #aux guide to ingress values
    aux_gd = input('Show auxiliar help?: [Y/N]:')
    if(aux_gd == 'Y'):
        dir = os.path.dirname(os.path.realpath(__file__))
        im = Image.open(dir + "\dimensiones.jpg")
        im.rotate(-90).show()
    elif(aux_gd == 'N'):
        None
    else:
        print('Wrong input, taking it as N') 
    #user_input
    try:
        mu_r_nucleo = float(input('\n\nRelative permeability of the core?  \n > '))
        w = float(input('\nCore thickness? [mm] \n > '))*1e-3
        da = float(input('\nLength of core section? [mm] \n > '))*1e-3
        wc = float(input('\nWidth of core section? [mm] \n > '))*1e-3
        g = float(input('\nLength of gap section? [mm] \n > '))*1e-3
        wg = float(input('\nWidth of gap section? [mm] \n > '))*1e-3
        n = float(input('\nNumber of turns in the coil?  \n > '))
        B = float(input('\nMagnetic Flux Density wanted in the gap? [mT] \n > '))*1e-3
    except:
        print('Wrong input')
        sys.exit()
elif(order == 'N'):
    #Dimensiones [m]Revisar dimensiones.jpg:Y
    l = 61e-3
    la = 29e-3
    lb = la
    lc = 33.5e-3
    d = 60e-3
    da = 32e-3
    g = 2e-3
    w = 10e-3 #espesor del nucleo
    wc = 31.5e-3
    wg = 2e-3
    #Constantes:
    mu_r_nucleo = 200000 #permeabilidad relativa del hierro
    n = 1000 #numero de vueltas bobina
    i = 0 #corriente que se desea despejar
    B = 200e-3 #campo magnetico a generar en Teslas
else:
    print('Wrong input')
    sys.exit()
mu_0 = (1.25)*10e-6 #permeabilidad en el vacio en Henrys/metro
#Calculos
Ac = w*wc #area transversal en metros cuadradosN
Ag = w*wg #area transversal en metros cuadrados
Rc = da/(mu_0*mu_r_nucleo*Ac) #reluctancia del nucleo
Rg = g/(mu_0*Ag) #reluctancia del gap
#Arnold & Garraud
ia = B*((da/mu_r_nucleo)+g)/(n*mu_0) #corriente [A] requerida para generar el campo en las dimensiones dadas
#Furlani
iF = B*((Ag/Ac)*(mu_0/mu_r_nucleo)*da+g)/(mu_0*n) #corriente [A] requerida para generar el campo en las dimensiones dadas 
print('\nThe Current needed is:',iF*1e3,'mA')
print('\nTo generate the Magnetic Flux Density of:',B*1e3,'mT')