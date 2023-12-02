# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços
frase = input('Digite uma frase: ').strip().lower()
palindromo = frase[::-1]

separador1 = frase.split()
uniao = ''.join(separador1)
separador2 = palindromo.split()
uniao2 = ''.join(separador2)

if uniao == uniao2:
    print('A frase É UM PALÍNDROMO')
else:
    print('A frase NÃO É UM PALÍNDROMO')


# Código curso em vídeo
frase1 = frase.lower()
palavras = frase1.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um Palíndromo')
else:
    print('A frase digitada não é um palíndromo')
