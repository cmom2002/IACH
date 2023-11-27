time_recipes = {
    1: [1, 1],
    2: [1, 1, 1],
    3: [1]
}

# Ordenar o dicionário com base no comprimento das listas de valores
sorted_time_recipes = dict(sorted(time_recipes.items(), key=lambda x: len(x[1]), reverse=True))

# Exibir o dicionário ordenado
print(sorted_time_recipes)