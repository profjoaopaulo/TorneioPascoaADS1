#1065 - TORNEIO DE PÁSCOA - PROGRAMAÇÃO E ALGORITMOS ADS I

#Vamos de while com lista!
numeros = []
i = 0 #var. de controle
pares = 0 #var. contador
while i <= 4: #note que a variável i acompanha os índices da lista
    numeros.append( int( input() ) )
    if numeros[i] % 2 == 0: #Par?
        pares += 1
    
    i += 1

print("%d valores pares" % pares)
