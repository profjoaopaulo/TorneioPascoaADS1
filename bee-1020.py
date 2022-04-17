#1020 - TORNEIO DE PÁSCOA - PROGRAMAÇÃO E ALGORITMOS ADS I

dias = int( input() )

#Anos? divisão inteira por 365
anos = dias//365
dias = dias%365 #atualizando dias com o que sobrou

#Meses? divisão por inteira por 30
meses = dias//30
dias = dias%30 #atualizando dias com o que sobrou

print("%d ano(s)" % anos)
print("%d mes(es)" % meses)
print("%d dia(s)" % dias)
