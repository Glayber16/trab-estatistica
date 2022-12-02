import matplotlib.pyplot as plt
import numpy as np
from time import time

x = np.zeros(10000) #vetor para guardar as variaveis geradas
w = np.zeros(10000)#vetor para guardar os valores geradao na distruibuição de Weibull
soma = 0 #variavel para ajudar na hora de retirar a média
somatorio = 0 #variavel para ajudar na hora da variancia 
λ = 1
β = 0.5

a = 13
c = 31
x[0] = time() #seed
m = 2**64


for i in range(1, 10000): # repetição 
    x[i] = (((a * x[i-1]) + c) % m) #formula para gerar variaveis aleatorias
    
x /= (m-1)

for i in range(10000):
    w[i] = (β/λ) * ((x[i]/λ) ** (β - 1)) * np.exp(-(x[i]/λ) ** β) #distribuição de Weibull
    

for i in range(10000):
    soma = soma + w[i] #calcular a media

media = soma/10000

for i in range(10000):
     somatorio = somatorio + (w[i] - media) ** 2 #calcular a variancia

variancia = somatorio/10000

plt.hist(w)#histograma
plt.show()#histograma

aux, bin = np.histogram(w)#Cdf
pdf = aux / sum(aux)#Cdf
cdf = np.cumsum(pdf)#Cdf
plt.plot(bin[1:], cdf)#Cdf
plt.show()#Cdf


print(f'Média = {media}')
print(f'Variancia = {variancia}')