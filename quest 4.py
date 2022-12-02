import matplotlib.pyplot as plt
import numpy as np
from time import time

x = np.zeros(10000) #vetor para guardar as variaveis geradas
n =np.zeros(10000) #vetor para receber as variaveis normais com media 0 e variancia 1
normal = np.zeros(10000) #vetor pra receber as variaveis normais com media 6 e variancia 4

soma = 0 #variavel para ajudar na hora de retirar a média
somatorio = 0 #variavel para ajudar na hora da variancia 

a = 13
c = 17
x[0] = time() #seed
m = 2**64


mi = 6 #media
var = 4 #variancia
y = 0 #distribuição normal com media 0 e variancia 1

for i in range(1,12):

    for i in range(1, 10000): # repetição 
        x[i] = (((a * x[i-1]) + c) % m)  #formula para gerar variaveis aleatorias
    
    x /= (m-1)

  
    n = (y + x - (m/2))/(np.sqrt(m/12)) #formula para gerar variaveis gaussianas com media 0 e variancia 1
   
    


normal = mi + (var ** 1/2) * n #formula para gerar variaveis gaussianas com media 6 e variancia 4

    

for i in range(10000):
    soma = soma + normal[i]#calcular a media

media = soma/10000
    
for i in range(10000):
    somatorio =  somatorio + (normal[i] - media) ** 2 #calcular a variancai

variancia = somatorio/10000

plt.hist(normal, bins=80)#histograma
plt.show()#histograma

aux, bin = np.histogram(normal)#Cdf
pdf = aux / sum(aux)#cdf
cdf = np.cumsum(pdf)#cdf
plt.plot(bin[1:], cdf)#cdf
plt.show()#cdf


print(f'Média = {media}')
print(f'Variancia = {variancia}')