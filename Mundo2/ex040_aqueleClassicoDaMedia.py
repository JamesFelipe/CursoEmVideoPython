# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo
# com a média atingida:

# Média abaixo de 5.0: Reprovado
# Média entre 5.0 e 6.9: Recuperação
# Média 7.0 ou superior: Aprovado

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print(f'Sua média é: {media} você foi REPROVADO')
elif media >= 5 and media <= 6.9:
    print(f'Sua média foi {media} você está em RECUPERAÇÃO')
elif media >= 7:
    print(f'Sua média foi {media} você foi APROVADO')
