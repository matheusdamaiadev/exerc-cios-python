
### 6. Considerando o histórico de transações listadas abaixo, apresente as seguintes informações:
# Agrupe as transações por tipo (entrada ou saída) e calcule o total de cada tipo.
# Agrupe as transações por categoria e calcule o total de cada categoria.
# Agrupe as transações por tipo e categoria, e calcule o total para cada combinação

transacoes = [
    {"tipo": "entrada", "categoria": "venda", "valor": 200},
    {"tipo": "saida", "categoria": "compra", "valor": 150},
    {"tipo": "entrada", "categoria": "servico", "valor": 300},
    {"tipo": "saida", "categoria": "compra", "valor": 100},
    {"tipo": "entrada", "categoria": "venda", "valor": 450},
    {"tipo": "saida", "categoria": "salario", "valor": 1200},
    {"tipo": "entrada", "categoria": "investimento", "valor": 800},
    {"tipo": "saida", "categoria": "aluguel", "valor": 900},
    {"tipo": "entrada", "categoria": "servico", "valor": 250},
    {"tipo": "saida", "categoria": "compra", "valor": 220},
]
soma_tipos = {}
for t in transacoes:
    tipo = t["tipo"]
    valor = t["valor"]
    if tipo not in soma_tipos:
        soma_tipos[tipo] = 0
    soma_tipos[tipo] += valor
print(f"{soma_tipos}")

soma_categorias = {}
for t in transacoes:
    categoria = t["categoria"]
    valor = t["valor"]
    if categoria not in soma_categorias:
        soma_categorias[categoria] = 0
    soma_categorias[categoria] += valor
print(f"{soma_categorias}")

tipo_e_categoria = {}

for t in transacoes:
    categoria = t["categoria"]
    valor = t["valor"]
    tipo = t["tipo"]

    if tipo not in tipo_e_categoria:
        tipo_e_categoria[tipo] = {}

    if categoria not in tipo_e_categoria[tipo]:
        tipo_e_categoria[tipo][categoria] = 0

    tipo_e_categoria[tipo][categoria] += valor

print(tipo_e_categoria)