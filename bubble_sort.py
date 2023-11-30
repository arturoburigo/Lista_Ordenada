def bubble_sort(arr):
    # Obtém o tamanho do array
    n = len(arr)
    
    # Loop externo para percorrer todo o array
    for i in range(n):
        # Loop interno para comparar elementos e fazer trocas
        for j in range(0, n - i - 1):
            # Verifica se o elemento atual é maior que o próximo
            if arr[j] > arr[j+1]:
                # Troca os elementos se estiverem fora de ordem
                temp = arr[j]  # Armazena temporariamente o elemento atual
                arr[j] = arr[j+1]  # Substitui o elemento atual pelo próximo
                arr[j+1] = temp  # Substitui o próximo pelo elemento temporário
    
    # Retorna o array ordenado após as iterações
    return arr

    

teste = bubble_sort([2,9,3,1,8,7])
print(teste)


