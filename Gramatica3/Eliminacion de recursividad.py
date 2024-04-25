def eliminar_recursividad_izquierda(gramatica):
    nueva_gramatica = {}

    for variable, producciones in gramatica.items():
        alfa = []
        beta = []

        for produccion in producciones:
            if produccion[0] == variable:
                alfa.append(produccion[1:])
            else:
                beta.append(produccion)

        if alfa:
            nueva_variable = variable + "'"
            nueva_gramatica[nueva_variable] = [x + [nueva_variable] for x in alfa] + [['ε']]
            nueva_gramatica[variable] = [x + [nueva_variable] for x in beta]
        else:
            nueva_gramatica[variable] = producciones

    return nueva_gramatica

gramatica_original = {
    'S': [['A', 'B','C'], ['S', 'uno']],
    'A': [['dos', 'B', 'C'],['ε']],
    'B': [['C', 'tres'], ['ε']],
    'C': [['cuatro', 'B'], ['ε']],
}

nueva_gramatica = eliminar_recursividad_izquierda(gramatica_original)

resultado = {}

for variable, producciones in nueva_gramatica.items():
    resultado[variable] = [list(p) for p in producciones]

print(resultado)