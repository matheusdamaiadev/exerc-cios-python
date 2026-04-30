
### 7. Considerando a lista de filmes abaixo, apresente as seguintes informações:
# Agrupe os filmes por gênero e liste os títulos de cada gênero.
# Agrupe os filmes por classificação indicativa e calcule a duração média dos filmes em cada classificação.
# Agrupe os filmes por gênero e liste os títulos classificados como "Mais de 120 min" e "120 min ou menos".

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

agrupamento_genero = {}
for filme in filmes:
    titulo = filme["titulo"]
    genero = filme["genero"]
    classificacao = filme["classificacao"]
    duracao = filme["duracao"]
    if genero not in agrupamento_genero:
        agrupamento_genero[genero] = []
    agrupamento_genero[genero].append(titulo)
print(f"{agrupamento_genero}")

agrupamento_class = {}
for filme in filmes:
    titulo = filme["titulo"]
    genero = filme["genero"]
    classificacao = filme["classificacao"]
    duracao = filme["duracao"]
    if classificacao not in agrupamento_class:
        agrupamento_class[classificacao] = {
            "tempo_total": 0,
            "n_de_filmes": 0
        }
    agrupamento_class[classificacao]["tempo_total"] += duracao
    agrupamento_class[classificacao]["n_de_filmes"] += 1

for classificacao, dados in agrupamento_class.items():
    total = dados["tempo_total"]
    numero_filmes = dados["n_de_filmes"]
    media_duracao = total / numero_filmes

    print(f"{classificacao}: {media_duracao}")

agrupamento_genero = {}
for filme in filmes:
    titulo = filme["titulo"]
    genero = filme["genero"]
    classificacao = filme["classificacao"]
    duracao = filme["duracao"]
    if genero not in agrupamento_genero:
        agrupamento_genero[genero] = {
            "dmais": [],
            "dmenos": []
        }
    if duracao > 120:
        agrupamento_genero[genero]["dmais"].append(titulo)
    else:
        agrupamento_genero[genero]["dmenos"].append(titulo)

for genero, maismenos in agrupamento_genero.items():
    dmais = agrupamento_genero[genero]["dmais"]
    dmenos = agrupamento_genero[genero]["dmenos"]
    print(f"{genero}: dura mais que 120  minutos: {', '.join(dmais)}. dura menos de 120 minutos: {', '.join(dmenos)}.")

