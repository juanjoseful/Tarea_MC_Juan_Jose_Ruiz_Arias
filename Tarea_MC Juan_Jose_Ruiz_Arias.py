#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import numpy as np


#random.uniform (a,b)

# elemento aleatorio que sigue la distribucion de gauss


def G(x):
    return (pow(x,2)-4)

def f(x):
    return(pow(np.sin(x),2))

# a es el limite inferior de la integral
# b es el limite superior de la integral
# M es el numero de puntos con los cuales iterar
# G es la funcion a iterar


# In[59]:


def monte_carlo(G, a, b, N):
    s = 0  #inicializo un contador para la sumatoria
    suma = 0
    p = np.random.uniform(0, N, 1) #funcion de importancia
    #aleatorios = random(0,10)
    for i in range(N):
        s += G(a + (b - a) * p) #funcion de importancia la uniforme
        suma += G(p)/p
        
    
    print(((b - a) / N) * s[0], '---> resultado con funcion de importancia lineal') 
    print(abs((1/N)*pow((G(p)/p),2) - pow(((1/N)*suma),2)), '------>error de Monte_Carlo')
   


# In[ ]:





# In[63]:


monte_carlo(G,0,10,1000)


# In[64]:


monte_carlo(f,0.5,1.7,1000)


# In[ ]:




