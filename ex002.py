funcionarios = [
    {"nome": "Ana", "setor": "Financeiro", "salario": 5000},
    {"nome": "João", "setor": "TI", "salario": 3000},
    {"nome": "Maria", "setor": "TI", "salario": 7000},
    {"nome": "Joana", "setor": "TI", "salario": 8750},
    {"nome": "José", "setor": "TI", "salario": 9300},
    {"nome": "Angela", "setor": "Financeiro", "salario": 2500},
    {"nome": "Carlos", "setor": "Financeiro", "salario": 2500},
    {"nome": "Bruno", "setor": "RH", "salario": 4200},
    {"nome": "Patricia", "setor": "RH", "salario": 6100},
    {"nome": "Marcos", "setor": "Financeiro", "salario": 5400},
]

# Para cada setor, some o Total de Salários e apresente o resultado.
# Apresente o total em salários e a média salarial para cada setor
# Funcionários por Setor e Faixa Salarial

totais = {}
contagem = {}

for f in funcionarios:
    setor = f["setor"]
    salario = f["salario"]
    totais[setor] = totais.get(setor, 0) + salario
    contagem[setor] = contagem.get(setor, 0) + 1
for setor in totais:
    total = totais[setor]
    qtd = contagem[setor]
    media = total / qtd

    print(f"{setor} -> Total: R${total:.2f} | Média: R${media:.2f}")