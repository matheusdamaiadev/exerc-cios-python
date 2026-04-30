
### 5. Dada a lista de alunos abaixo, extraia as seguintes informações:
# Alunos por Turma e Aprovação
# Agrupe os alunos por turma e liste os nomes de cada turma
# Agrupe os alunos por turma e calcule a média de notas de cada turma
# Agrupe os alunos por "Nota Acima de 7" e "Nota 7 ou abaixo" e liste os nomes dos alunos e a sua respectiva nota em cada categoria

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
agrupamento_turma = {}
for aluno in alunos:
    nome = aluno["nome"]
    turma = aluno["turma"]
    nota = aluno["nota"]
    if turma not in agrupamento_turma:
        agrupamento_turma[turma] = {
            "nomes": [],
            "nota_somada_turma": 0,
            "quantidade_alunos_turma": 0
        }
    agrupamento_turma[turma]["nomes"].append(nome)
    agrupamento_turma[turma]["nota_somada_turma"] += nota
    agrupamento_turma[turma]["quantidade_alunos_turma"] += 1
for turma, dados in agrupamento_turma.items():
    quantidade = dados["quantidade_alunos_turma"]
    soma = dados ["nota_somada_turma"]
    media = soma / quantidade
    print(f"{turma}: nomes={dados['nomes']}, média={media:.2f}")


nota_mais_7 = []
nota_menos_7 = []

for aluno in alunos:
    nome = aluno["nome"]
    nota = aluno["nota"]
    if nota > 7:
        nota_mais_7.append({"nome": nome, "nota": nota})
    else:
        nota_menos_7.append({"nome": nome, "nota": nota})
print(f"mais de 7: {nota_mais_7}")
print(f"7 ou menos: {nota_menos_7}")