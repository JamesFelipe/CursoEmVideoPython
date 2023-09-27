# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária
# para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area_tinta = (largura * altura) / 2
print(f'Uma parede com larugra {largura}m² e {altura}m² precisa de {area_tinta} litros de tinta')
