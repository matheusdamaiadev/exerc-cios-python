# Exercícios

### 1. Considerando os dados abaixo, apresente as seguintes informações:
- Agrupar por Categoria e somar os valores vendidos
- Agrupar por Categoria e listar os produtos vendidos
```json
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
```
### 2. Abaixo há uma lista de funcionários com seus respectivos setores e salários. Apresente os seguintes dados:
- Para cada setor, some o Total de Salários e apresente o resultado.
- Apresente o total em salários e a média salarial para cada setor
- Funcionários por Setor e Faixa Salarial
```json
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
```

### 3. Dada a lista de pets abaixo, extraia as seguintes informações:
- Agrupe os pets por espécie e liste os nomes de cada espécie
- Agrupe os pets por espécie e calcule o peso médio de cada espécie
- Agrupe os pets por espécie e liste os nomes dos pets que pesam "Mais de 10 Kg" e "10 Kg ou menos"
```json
pets = [
    {"nome": "Thor", "especie": "Cachorro", "peso": 12},
    {"nome": "Mimi", "especie": "Gato", "peso": 4},
    {"nome": "Rex", "especie": "Cachorro", "peso": 30},
    {"nome": "Luna", "especie": "Gato", "peso": 6},
    {"nome": "Bob", "especie": "Cachorro", "peso": 9},
    {"nome": "Mel", "especie": "Gato", "peso": 5},
    {"nome": "Nina", "especie": "Coelho", "peso": 3},
    {"nome": "Pipoca", "especie": "Coelho", "peso": 2},
    {"nome": "Max", "especie": "Cachorro", "peso": 18},
    {"nome": "Fred", "especie": "Papagaio", "peso": 1},
]
```

### 4. Considerando a lista de pedidos abaixo, apresente as seguintes informações:
- Agrupe os pedidos por cidade e conte quantos pedidos foram entregues e quantos estão pendentes em cada cidade.
- Agrupe os pedidos por status e liste as cidades onde os pedidos foram entregues e onde estão pendentes.
```json
pedidos = [
    {"id": 1, "cidade": "Joinville", "status": "entregue"},
    {"id": 2, "cidade": "Joinville", "status": "pendente"},
    {"id": 3, "cidade": "Araquari", "status": "entregue"},
    {"id": 4, "cidade": "Joinville", "status": "entregue"},
    {"id": 5, "cidade": "Araquari", "status": "pendente"},
    {"id": 6, "cidade": "São Francisco do Sul", "status": "entregue"},
    {"id": 7, "cidade": "Jaraguá do Sul", "status": "pendente"},
    {"id": 8, "cidade": "Joinville", "status": "pendente"},
    {"id": 9, "cidade": "Araquari", "status": "entregue"},
    {"id": 10, "cidade": "Jaraguá do Sul", "status": "entregue"},
]
```

### 5. Dada a lista de alunos abaixo, extraia as seguintes informações:
- Alunos por Turma e Aprovação
- Agrupe os alunos por turma e liste os nomes de cada turma
- Agrupe os alunos por turma e calcule a média de notas de cada turma
- Agrupe os alunos por "Nota Acima de 7" e "Nota 7 ou abaixo" e liste os nomes dos alunos e a sua respectiva nota em cada categoria
```json
alunos = [
    {"nome": "Lucas", "turma": "A", "nota": 8},
    {"nome": "Fernanda", "turma": "A", "nota": 5},
    {"nome": "Pedro", "turma": "B", "nota": 6},
    {"nome": "Julia", "turma": "B", "nota": 9},
    {"nome": "Mariana", "turma": "A", "nota": 7},
    {"nome": "Gabriel", "turma": "B", "nota": 4},
    {"nome": "Aline", "turma": "C", "nota": 10},
    {"nome": "Rafael", "turma": "C", "nota": 6},
    {"nome": "Bianca", "turma": "A", "nota": 9},
    {"nome": "Tiago", "turma": "C", "nota": 8},
]
```

### 6. Considerando o histórico de transações listadas abaixo, apresente as seguintes informações:
- Agrupe as transações por tipo (entrada ou saída) e calcule o total de cada tipo.
- Agrupe as transações por categoria e calcule o total de cada categoria.
- Agrupe as transações por tipo e categoria, e calcule o total para cada combinação
```json
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
```

### 7. Considerando a lista de filmes abaixo, apresente as seguintes informações:
- Agrupe os filmes por gênero e liste os títulos de cada gênero.
- Agrupe os filmes por classificação indicativa e calcule a duração média dos filmes em cada classificação.
- Agrupe os filmes por gênero e liste os títulos classificados como "Mais de 120 min" e "120 min ou menos".
```json
filmes = [
    {"titulo": "Aventura Final", "genero": "Ação", "classificacao": "14", "duracao": 130},
    {"titulo": "Risos em Dobro", "genero": "Comédia", "classificacao": "10", "duracao": 95},
    {"titulo": "Noite de Mistério", "genero": "Suspense", "classificacao": "16", "duracao": 110},
    {"titulo": "Coração em Cena", "genero": "Romance", "classificacao": "12", "duracao": 125},
    {"titulo": "Missão Oceânica", "genero": "Ação", "classificacao": "12", "duracao": 118},
    {"titulo": "Férias Malucas", "genero": "Comédia", "classificacao": "Livre", "duracao": 102},
    {"titulo": "Segredos da Cidade", "genero": "Suspense", "classificacao": "14", "duracao": 140},
    {"titulo": "Destino de Verão", "genero": "Romance", "classificacao": "10", "duracao": 98},
    {"titulo": "Heróis do Amanhã", "genero": "Ação", "classificacao": "14", "duracao": 145},
    {"titulo": "Amigos do Bairro", "genero": "Comédia", "classificacao": "Livre", "duracao": 88},
]
```