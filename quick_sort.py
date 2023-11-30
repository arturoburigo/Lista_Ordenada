# Parte 1 - Função para particionar o array
def particao(array, inicio, final):
    pivo = array[final]
    i = inicio - 1
    
    for j in range(inicio, final):
        if array[j] <= pivo:
            i += 1
            array[i], array[j] = array[j], array[i]
    
    array[i + 1], array[final] = array[final], array[i + 1]
    return i + 1

# Parte 2 - Função para ordenar usando Quick Sort
def quick_sort(array, inicio, final):
    if inicio < final:
        posicao = particao(array, inicio, final)
        # Ordena a parte esquerda do pivô
        quick_sort(array, inicio, posicao - 1)
        # Ordena a parte direita do pivô
        quick_sort(array, posicao + 1, final)
    return array

# Exemplo de uso:
vetor = [12, 11, 13, 5, 6, 7]
resultado = quick_sort(vetor, 0, len(vetor) - 1)
print("Lista ordenada:", resultado)
