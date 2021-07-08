#Aluna: Noani Barbieri
#Materia: Eletronica Basica 
#LAB 01

#Definindo a biblioteca
import math
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi
from scipy import signal

#valores tabela 01
#id = np.array([0,0.0008,3.2853,5.7492,8.2260,10.709,13.195,15.684,18.175,20.66,23.159])
#vd = np.array([0,651.53,685.86,700.34,709.60,716.43,721.83,726.29,730.11,733.43,736.37])

#valores tabela 02
id = np.array([0,-5.01,-10.01,-15.01,-20.01,-25.01,-30.01,-35.01,-40.01,-45.01,-50.01,-55.01,-60.01])
vd = np.array([0,-2.5,-5,-7.5,-10,-12.5,-15,-17.5,-20,-22.5,-25,-27.5,-30])

#plotando os graficos
fig, ax1 = plt.subplots(1, 1)
plt.style.use('ggplot')
plt.title('Curva característica de um diodo V x I', fontsize=12, fontweight='bold', fontstyle='italic')
ax1.plot(vd, id, 'r-', linewidth=2, color='Blue')
plt.xlabel("Voltagem(Vd)",fontsize=10, fontfamily='serif')
plt.ylabel("Corrente(Id)",fontsize=10,fontfamily='serif')
plt.grid(True)
plt.show()




