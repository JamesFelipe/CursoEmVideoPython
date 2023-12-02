# Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu atatus, de acordo com a tabela abaixo

# Abaixo de 18.5: abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: sobrepeso
# 30 até 40: obesidade
# acima de 40: Obsidade mórbida

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)  

if imc >= 18.5 and imc < 25:
    print(f'Seu IMC é {imc:.2f} você está no PESO IDEAL')
elif imc >= 25 and imc < 30:
    print(f'Seu IMC é {imc:.2f} você está com SOBREPESO')
elif imc >= 30 and imc < 40:
    print(f'Seu IMC é {imc:.2f} Você está com OBSIDADE')
elif imc > 40:
    print(f'Seu IMC é: {imc:.2f} você está com OBSIDADE MÓRBIDA')
