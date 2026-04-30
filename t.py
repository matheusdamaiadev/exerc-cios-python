#list: guardam itens em sequencia
nomes = ["Ana", "João", "Maria"]
#dict: Guardam dados no formato chave → valor
pessoa = {"nome": "Ana", "idade": 25}# "chave": "valor"


#Agrupamento de dados: É organizar informações semelhantes juntas.
compras = [
    {"produto": "Arroz", "categoria": "Alimento"},
    {"produto": "Feijão", "categoria": "Alimento"},
    {"produto": "Shampoo", "categoria": "Higiene"}
]
#Agrupar significa transformar isso em algo como:
{
    "Alimento": ["Arroz", "Feijão"],
    "Higiene": ["Shampoo"]
}

#Padrão para agrupamento de dados: Se a chave não existe → cria uma lista. Depois adiciona o valor:

#if chave not in dicionario:
#    dicionario[chave] = []
#dicionario[chave].append(valor)

#exemplo real:
dados = [
    {"nome": "Ana", "setor": "Financeiro"},
    {"nome": "João", "setor": "TI"},
    {"nome": "Maria", "setor": "TI"}
]

agrupados = {}

for pessoa in dados:
    setor = pessoa["setor"]     # pega a categoria
    nome = pessoa["nome"]       # pega o valor

    if setor not in agrupados:  # se não existe
        agrupados[setor] = []   # cria lista

    agrupados[setor].append(nome)  # adiciona nome

print(agrupados)


#somar valores por chave: É acumular valores de acordo com uma categoria.

gastos = [
    {"categoria": "Alimento", "valor": 50},
    {"categoria": "Alimento", "valor": 30},
    {"categoria": "Transporte", "valor": 20}
]
 #transformar em:
{
    "Alimento": 80,
    "Transporte": 20
}


#padrão de soma: Se não existe, começa em 0. Se existe, soma:

#dicionario[chave] = dicionario.get(chave, 0) + valor

#exemplo real:
gastos = [
    {"categoria": "Alimento", "valor": 50},
    {"categoria": "Alimento", "valor": 30},
    {"categoria": "Transporte", "valor": 20}
]

total = {}

for item in gastos:
    categoria = item["categoria"]
    valor = item["valor"]

    total[categoria] = total.get(categoria, 0) + valor

print(total)

#Padrão principal: “Se não existe, cria. Se existe, atualiza.”

#somar e agrupar juntos: 
vendas = [
    {"produto": "Notebook", "categoria": "Eletrônico", "valor": 3000},
    {"produto": "Mouse", "categoria": "Eletrônico", "valor": 100},
    {"produto": "Cadeira", "categoria": "Móvel", "valor": 500}
]

resultado = {}

for venda in vendas:
    categoria = venda["categoria"]
    produto = venda["produto"]
    valor = venda["valor"]

    if categoria not in resultado:
        resultado[categoria] = {
            "produtos": [],
            "total": 0
        }

    resultado[categoria]["produtos"].append(produto)
    resultado[categoria]["total"] += valor

print(resultado)


#desafio 1;
#Objetivo: agrupar nomes por cidade
dados = [
    {"nome": "Ana", "cidade": "SP"},
    {"nome": "João", "cidade": "RJ"},
    {"nome": "Maria", "cidade": "SP"}
]

agrupados = {}

for dado in dados:
    nome = dado["nome"]
    cidade = dado["cidade"]
    if cidade not in agrupados:
        agrupados[cidade] = []
    agrupados[cidade].append(nome)
    print(f"{agrupados}")
    

#desafio 2;
#somar valores por produto

vendas = [
    {"produto": "Camisa", "valor": 50},
    {"produto": "Camisa", "valor": 30},
    {"produto": "Calça", "valor": 100}
]

totais = {}

for v in vendas:
    p = v["produto"]
    val = v["valor"]
    totais[p] = totais.get(p, 0) + val
print(f"{totais}")

#desafio final
#Gerar:Total gasto por cliente e Lista de produtos comprados por cliente

vendas = [
    {"cliente": "Ana", "produto": "Notebook", "valor": 3000},
    {"cliente": "Ana", "produto": "Mouse", "valor": 100},
    {"cliente": "João", "produto": "Teclado", "valor": 200},
    {"cliente": "Ana", "produto": "Cadeira", "valor": 500}
]

dados = {}

for venda in vendas:
    cliente = venda["cliente"]
    produto = venda["produto"]
    valor = venda["valor"]
    if cliente not in dados:
        dados[cliente] = {
            "produtos": [],
            "total": 0
        }
    dados[cliente]["produtos"].append(produto)
    dados[cliente]["total"] += valor
print(f"{dados}")


#ordenar dados: crescente ou decrescente EX: [5, 2, 9, 1] → [1, 2, 5, 9]
#para pegar o maior ou menor numero podemos Ordenar tudo e pegar o primeiro/último Ou usar funções como max() (veremos depois)


#fundamentos
#sorted() = Função que ordena dados: numeros = [5, 2, 9, 1] ordenado = sorted(numeros)
#reverse=True = Para inverter (maior → menor): sorted(numeros, reverse=True)
#key Define por qual critério ordenar pessoas = ["Ana", "João", "Maria"] sorted(pessoas, key=len)       *(tamanho do nome)
#lambda = Uma função rápida, usada dentro do key: lambda x: x[1]. “para cada item, use o segundo valor como critério”



#Exemplos

#ordenar números

numeros = [5, 2, 9, 1]

ordenados = sorted(numeros)

print(ordenados)



#ordenar dicionário por valor

vendas = {
    "Ana": 500,
    "João": 300,
    "Maria": 800
}

ordenado = sorted(vendas.items(), key=lambda item: item[1])

print(ordenado)

#pegar top 3 maiores valores
ordenado = sorted(vendas.items(), key=lambda x: x[1], reverse=True)

top3 = ordenado[:3]

print(top3)


#lista de dicionários (caso real)

vendas = [
    {"cliente": "Ana", "valor": 500},
    {"cliente": "João", "valor": 300},
    {"cliente": "Maria", "valor": 800}
]

ordenado = sorted(vendas, key=lambda x: x["valor"], reverse=True)

print(ordenado)



#Desafio: Ordenar clientes por valor gasto:

dados = {
    "Ana": 200,
    "João": 500,
    "Maria": 300
}

ordenado = sorted(dados.items(), key=lambda x: x[1] , reverse=True)

print(f"{ordenado}")


numeros = [8, 2, 5, 1, 9]#ordenar em ordem crescente

ordenado = sorted(numeros)
print(f"{ordenado}")




#ordenar pelo valor: maior menor
produtos = {
    "teclado": 150,
    "mouse": 80,
    "monitor": 900
}

ordenado = sorted(produtos.items(), key=lambda x: x[1] , reverse=True)
print(f"{ordenado}")


valores = [100, 450, 200, 800, 50]#pegar os dois maiores

ordenado = sorted(valores, reverse=True)
top2 = ordenado[:2]
for i in top2:
    print(f"{i}")

vendas = [
    {"cliente": "Ana", "categoria": "Eletrônicos", "valor": 500},
    {"cliente": "João", "categoria": "Roupas", "valor": 200},
    {"cliente": "Ana", "categoria": "Eletrônicos", "valor": 300},
    {"cliente": "Maria", "categoria": "Roupas", "valor": 400},
    {"cliente": "João", "categoria": "Eletrônicos", "valor": 700},
]

#Agrupar por categoria
#Somar os valores
#Ordenar do maior para o menor
#Mostrar o top 2 categorias
totais = {}
for v in vendas:
    p = v["categoria"]
    val = v["valor"]
    totais[p] = totais.get(p, 0) + val
print(f"{totais}")
ordenado = sorted(totais.items(), key=lambda x: x[1], reverse=True)
print(f"{ordenado}")



#filtrar pelo nome do produto


produtos = [
    {"nome": "Mouse", "preco": 50},
    {"nome": "Teclado", "preco": 100},
]

produto_procurado = "Teclado"
preco_produto = 0

for p in produtos:
    
    if p["nome"] == produto_procurado:
        preco_produto = preco_produto + p["preco"]
print(f"{preco_produto}")



vendas = [
    {"cliente": "Ana", "categoria": "Eletronico", "valor": 1200},
    {"cliente": "João", "categoria": "Roupas", "valor": 200},
    {"cliente": "Ana", "categoria": "Eletronico", "valor": 800},
    {"cliente": "Maria", "categoria": "Eletronico", "valor": 1500},
    {"cliente": "João", "categoria": "Eletronico", "valor": 2000},
]

#Filtrar apenas categoria "Eletronico"
#Agrupar por cliente
#Somar valores
#Criar ranking do maior para o menor

vendas = [
    {"cliente": "Ana", "categoria": "Eletronico", "valor": 1200},
    {"cliente": "João", "categoria": "Roupas", "valor": 200},
    {"cliente": "Ana", "categoria": "Eletronico", "valor": 800},
    {"cliente": "Maria", "categoria": "Eletronico", "valor": 1500},
    {"cliente": "João", "categoria": "Eletronico", "valor": 1000},
]

#Filtrar apenas categoria "Eletronico"
#Agrupar por cliente
#Somar valores
#Criar ranking do maior para o menor



grupo_eletronico = {}

for v in vendas:
    categoria = v["categoria"]
    cliente = v["cliente"]
    valor = v["valor"]

    if categoria == "Eletronico":
        grupo_eletronico[cliente] = grupo_eletronico.get(cliente, 0) + valor

ordenado = sorted(grupo_eletronico.items(), key=lambda x: x[1], reverse=True)

for posicao, (cliente, total) in enumerate(ordenado, start=1):
    print(f"{posicao}º - {cliente}: R${total:.2f}")








    vendas = [
    {"tipo": "online", "produto": "camisa", "valor": 100},
    {"tipo": "loja", "produto": "calça", "valor": 150},
    {"tipo": "online", "produto": "camisa", "valor": 200},
    {"tipo": "loja", "produto": "sapato", "valor": 300},
    {"tipo": "online", "produto": "sapato", "valor": 250},
    {"tipo": "loja", "produto": "calça", "valor": 100},
    {"tipo": "online", "produto": "camisa", "valor": 150},
    {"tipo": "loja", "produto": "camisa", "valor": 120},
]


agrupadasso = {}
for venda in vendas :
    tipo = venda["tipo"]
    produto = venda["produto"]
    valor = venda["valor"]
    if tipo not in agrupadasso:
        agrupadasso[tipo] = {}
    
    if produto not in agrupadasso[tipo]:
        agrupadasso[tipo][produto] = 0

    agrupadasso[tipo][produto] += valor

print(f"{agrupadasso}")