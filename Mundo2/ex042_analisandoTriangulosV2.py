# Refaça o desafio 035 dos triângulos acrescentando o recurso de mostrar que tipo de triângulo será formador:

# Equilátero: todos os lados iguais
# isósceles: dois lados iguas
# escaleno: todos os lados diferentes

reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('É um triângulo')
    if reta1 != reta2 != reta3:
        print('Triângulo Escaleno')
    elif reta1 == reta2 != reta3 or reta2 == reta1 != reta3 or reta3 == reta2 != reta1:
        print('Triângulo Isósceles')
    else:
        print('Triângulo Equilátero')
else:
    print('Não é um triângulo')
