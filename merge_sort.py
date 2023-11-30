def merge_sort(array):
    if len(array) > 1:
        meio = len(array) // 2  # Encontra o ponto médio da lista
        esquerda = array[:meio]  # Divide a lista em duas metades
        direita = array[meio:]

        # Recursivamente ordena as duas metades
        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0

        # Merge das duas metades ordenadas
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                array[k] = esquerda[i]
                i += 1
            else:
                array[k] = direita[j]
                j += 1
            k += 1

        # Adiciona os elementos restantes da lista esquerda, se houver
        while i < len(esquerda):
            array[k] = esquerda[i]
            i += 1
            k += 1

        # Adiciona os elementos restantes da lista direita, se houver
        while j < len(direita):
            array[k] = direita[j]
            j += 1
            k += 1

    return array

# Exemplo de uso:
array = [12, 11, 13, 5, 6, 7]
resultado = merge_sort(array)
print("Lista ordenada:", resultado)
