# Faça um algoritmo que leia o comprimento do cateto oposto e do cateto adjacente de triângulo retângulo, 
# calcule e mostre o comprimento da hipotenusa
from math import hypot
cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
print(f'Então a hypotenusa do triângulo retângulo é: {hypot(cateto_oposto, cateto_adjacente):.2f}')

