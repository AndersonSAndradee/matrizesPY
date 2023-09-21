'''Função = soma matrizes, "recebe como parâmetro matriz1 e matriz2, se as matrizes possuem mesmas proporções retorna o valor da soma delas, caso contrário retorna o valor False" '''
def soma_matrizes(m1, m2): 
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):  # Compara se é válido a soma das matrizes
        matriz_final = []  # Inicializa a matriz final vazia

        for i in range(len(m1)):
            linha_resultado = []  # Inicializa uma lista vazia para a matriz final
            for j in range(len(m1[0])):
                
                elemento1 = m1[i][j]
                elemento2 = m2[i][j]
                
                soma = elemento1 + elemento2
                linha_resultado.append(soma)  # Adiciona o resultado à linha da matriz final
                
            matriz_final.append(linha_resultado)  # Adiciona a linha à matriz final

        return matriz_final
    else:
        return False
