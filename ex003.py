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
# Agrupe os pets por espécie e liste os nomes de cada espécie
# Agrupe os pets por espécie e calcule o peso médio de cada espécie
# Agrupe os pets por espécie e liste os nomes dos pets que pesam "Mais de 10 Kg" e "10 Kg ou menos"

agrupamento_por_especie = {}

for pet in pets:
    nome = pet["nome"]
    especie = pet["especie"]
    peso = pet ["peso"]
   
    if especie not in agrupamento_por_especie:
        agrupamento_por_especie[especie] = {
            "peso_total": 0,
            "nomes": [],
            "quantidade" : 0,
            "mais_10": [],
            "menos_10": []
        }
    agrupamento_por_especie[especie]["nomes"].append(nome)
    agrupamento_por_especie[especie]["peso_total"] += peso
    agrupamento_por_especie[especie]["quantidade"] += 1
    if peso > 10:
        agrupamento_por_especie[especie]["mais_10"].append(nome)
    else:
        agrupamento_por_especie[especie]["menos_10"].append(nome)

for especie, dados in agrupamento_por_especie.items():
    media = dados["peso_total"] / dados["quantidade"]

    print(f"{especie}: nomes: {dados['nomes']}, n de animais: {dados['quantidade']}, peso médio: {media}. mais de 10kg: {dados['mais_10']}. menos de 10kg:{dados['menos_10']} ")

