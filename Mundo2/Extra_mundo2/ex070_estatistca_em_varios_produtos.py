# Declaração de variáveis
total_gasto = 0
produtos_caros = 0
produto_mais_barato = None
nome_produto_mais_barato = None

# Laço while
while True:
    # Lê o nome e o valor do produto
    nome_produto = input("Digite o nome do produto: ")
    valor_produto = float(input("Digite o valor do produto: R$ "))

    # Atualiza o total de gasto
    total_gasto += valor_produto

    # Verifica se o produto é caro que mil reais
    if valor_produto > 1000:
        produtos_caros += 1

    # Atualiza o produto mais barato
    if produto_mais_barato is None or valor_produto < produto_mais_barato:
        produto_mais_barato = valor_produto
        nome_produto_mais_barato = nome_produto

    # Pergunta se o usuário quer continuar
    continuar = input("Quer continuar: (S/N) ")
    if continuar.upper() == "N":
        break

# Imprime os resultados
print(f"O total de gasto na compra foi de R$ {total_gasto}")
print(f"Existem {produtos_caros} produtos que custam mais de R$1000")
print(f"O produto mais barato é o {nome_produto_mais_barato} com o valor de R$ {produto_mais_barato}")
