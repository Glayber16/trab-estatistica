import matplotlib.pyplot as plt
import numpy as np
from time import time

x = np.zeros(10000) #vetor 0 a 1
vet = np.zeros(10000) #vetor 4 a 12

soma = 0 #variavel para ajudar na hora de retirar a média
somatorio = 0 #variavel para ajudar na hora da variancia 

a = 13
c = 15
x[0] = time() #seed
m = 2**32

if a < m and c < m: #condição da formula

    for i in range(1, 10000): # repetição 
        x[i] = (((a * x[i-1]) + c) % m) 

    
    x /= (m - 1)

    vet = (x * 8) + 4

    

    for i in range(10000):
        soma = vet[i] + soma

    media = soma/10000

    for i in range(10000): #para a variancia
        
        somatorio = somatorio + (vet[i] - media) ** 2 #calculo da variancia
        
    variancia = somatorio/10000


else:
    print('Digite valores validos!!')


plt.hist(vet)
plt.show()#histograma

aux, bin = np.histogram(vet)#Cdf
pdf = aux / sum(aux)#Cdf
cdf = np.cumsum(pdf)#Cdf
plt.plot(bin[1:], cdf)#Cdf
plt.show()#Cdf

print(f'media =  {media}') # printar a média
print(f'variancia = {variancia}') # printar a variancia