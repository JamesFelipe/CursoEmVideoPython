# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import radians, sin, cos, tan
angulo = float(input('Digite um ângulo: '))
print(f'O seno de {angulo} é: {sin(radians(angulo)):.2f}')
print(f'O cosseno de {angulo} é: {cos(radians(angulo)):.2f}')
print(f'A tangente de {angulo} é: {tan(radians(angulo)):.2f}')
