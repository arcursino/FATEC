G = {1:['B'], 2:['A', 'B', 'E', 'F'], 3:['A', 'B', 'C'], 4:['B', 'E'], 5:['B', 'E', 'F']}

while G: #enquanto o grafo não é vazio
    print (G)
    maquina_dificil = sorted(G, key=lambda x: len(G[x])) [0]
    operario = G[maquina_dificil] [0]
    print (f'Casou {maquina_dificil} com {operario}')
    del G[maquina_dificil]
    for m in G:
        if operario in G[m]: G[m].remove(operario)