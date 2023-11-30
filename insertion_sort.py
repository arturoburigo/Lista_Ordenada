def insertion_sort(array):
    # Obtém o comprimento do array
    n = len(array)
    
    # Percorre o array começando do segundo elemento
    for i in range(1, n):
        # Armazena o valor atual para posterior comparação
        marcado = array[i]
        
        # Define o índice para comparação com o elemento marcado
        j = i - 1
        
        # Compara o elemento marcado com os elementos anteriores e os move para frente
        while j >= 0 and marcado < array[j]:
            array[j + 1] = array[j]  # Move os elementos maiores para frente
            j -= 1  # Decrementa o índice para comparar com elementos anteriores
        
        # Coloca o elemento marcado na posição correta
        array[j + 1] = marcado
        
    return array

# Chama a função e imprime o resultado
teste = insertion_sort([2, 9, 3, 1, 8])
print(teste)
