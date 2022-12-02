import matplotlib.pyplot as plt
import numpy as np
from time import time

x = np.zeros(10000)#vetor para guardar as variaveis geradas
inv = np.zeros(10000)
soma = 0 #variavel para ajudar na hora de retirar a média
somatorio = 0 #variavel para ajudar na hora da variancia 
λ = 3
a = 3
c = 0.1
x[0] = time() #seed
m = 2**64



for i in range(1, 10000): # repetição 
    x[i] = (((a * x[i-1]) + c) % m)  #formula para gerar as variaveis aleatorias
    
x /= (m-1)

for i in range(10000):
    inv[i] = (-1/λ) * np.log(1 - x[i]) #CDF inversa


for i in range(10000):
    soma = inv[i] + soma

media = soma/10000 #media amostral


for i in range(10000):
    somatorio = somatorio + (inv[i] - media) ** 2
    
variancia = somatorio/10000 #variancia amostral

plt.hist(inv)#histograma
plt.show()#histograma

aux, bin = np.histogram(inv)#Cdf
pdf = aux / sum(aux)#Cdf
cdf = np.cumsum(pdf)#Cdf
plt.plot(bin[1:], cdf)#Cdf
plt.show()#Cdf


mediat = 1/λ #media teorica
varianciat = 1/λ ** 2 # variancia teorica

print(f'Media Teorica = {mediat}')
print(f'Variancia Teorica = {varianciat}')   

print(f'media = {media}')
print(f'variancia = {variancia}')