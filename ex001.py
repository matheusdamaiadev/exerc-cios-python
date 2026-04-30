vendas = [
    {"produto": "Notebook", "categoria": "Eletrônicos", "valor": 3000},
    {"produto": "Smartphone", "categoria": "Eletrônicos", "valor": 1500},
    {"produto": "Cadeira", "categoria": "Móveis", "valor": 500},
    {"produto": "Mesa", "categoria": "Móveis", "valor": 1200},
    {"produto": "Fone de Ouvido", "categoria": "Eletrônicos", "valor": 200},
    {"produto": "Monitor", "categoria": "Eletrônicos", "valor": 950},
    {"produto": "Teclado", "categoria": "Eletrônicos", "valor": 180},
    {"produto": "Sofá", "categoria": "Móveis", "valor": 2300},
    {"produto": "Estante", "categoria": "Móveis", "valor": 800},
    {"produto": "Impressora", "categoria": "Eletrônicos", "valor": 650},
]
#Agrupar por Categoria e somar os valores vendidos
# Agrupar por Categoria e listar os produtos vendidos
produtos = {}

for venda in vendas:
    categoria = venda["categoria"]
    produto = venda["produto"]
    valor = venda["valor"]

    if categoria not in produtos:
            produtos[categoria] = []

    produtos[categoria].append(produto)
    
for p in produtos:
      print(f"{p} : {', '.join(produtos[p])}")


totais = {}

for venda in vendas:
    valor = venda["valor"]
    categoria = venda["categoria"]
    if categoria not in totais:
          totais[categoria] = 0
    totais[categoria] += valor

for t in totais:
    print(f"{t}: {totais[t]}")