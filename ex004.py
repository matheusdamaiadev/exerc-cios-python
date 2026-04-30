#4. Considerando a lista de pedidos abaixo, apresente as seguintes informações:
# Agrupe os pedidos por cidade e conte quantos pedidos foram entregues e quantos estão pendentes em cada cidade.
#Agrupe os pedidos por status e liste as cidades onde os pedidos foram entregues e onde estão pendentes.

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
agrupamento_cidade = {}

for pedido in pedidos:
    pedido_id = pedido["id"]
    cidade = pedido["cidade"]
    status = pedido["status"]

    if cidade not in agrupamento_cidade:
        agrupamento_cidade[cidade] = {
            "total_pedidos": 0,
            "lista_pedidos_e": [],
            "lista_pedidos_p":[],
            "pedidos_p": 0,
            "pedidos_e": 0
        }
    agrupamento_cidade[cidade]["total_pedidos"] += 1
    if status == "entregue":
        agrupamento_cidade[cidade]["pedidos_e"] += 1
        agrupamento_cidade[cidade]["lista_pedidos_e"].append(pedido_id)
    else:
        agrupamento_cidade[cidade]["pedidos_p"] += 1
        agrupamento_cidade[cidade]["lista_pedidos_p"].append(pedido_id)
print(f"{agrupamento_cidade}")


agrupamento_status = {}
for pedido in pedidos:
    status = pedido["status"]
    cidade = pedido["cidade"]
    if status not in agrupamento_status:
        agrupamento_status[status] = set()#set nao deixa repetir as cidades
    agrupamento_status[status].add(cidade)#.add pcausa do set (set nao e uma lista)
print(f"{agrupamento_status}")