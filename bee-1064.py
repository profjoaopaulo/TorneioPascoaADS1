#1064 - TORNEIO DE PÁSCOA - PROGRAMAÇÃO E ALGORITMOS ADS I

#Bora armazenar os valores numa lista!
numeros = []
i = 0 #variável de controle para o laço while
numPositivos = 0 #variável do tipo contador para contar quantos positivos tem na lista
media = 0 #variável do tipo somatório para somar todos os valores positivos da lista
while i <= 5: #com as configurações para a variável de controle i, limitamos para 6 o número de repetições para o laço
    numeros.append( float( input() ) ) #convertendo para float, pois os números podem ser de ponto flutuante
    if numeros[i] > 0: #verificando se o número armazenado na lista é positivo
        numPositivos += 1 #contando mais um positivo!
        media += numeros[i] #somando os números positivos armazenados na lista
    
    i += 1 #configurando próximo valor para a variável de controle

print("%d valores positivos" % numPositivos)
print("%.1f" % (media/numPositivos)) #calculando e imprimindo a média dos valores positivos da lista
